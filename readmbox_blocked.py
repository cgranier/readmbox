import mailbox
import re
import csv


mbox_file = "data/BLOCKED.mbox"
mbox = mailbox.mbox(mbox_file)

def getbody(message): #getting plain text 'email body'
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
    return body

def main():
    total_messages = 1
    claim_list_file = "data/block_list.csv"
    with open(claim_list_file, 'w', newline='', encoding='utf-8') as new_file:
        out_file_headers = ['channel_name','video_title','copyrighted_content','claimed_by','claim_note','claim_url','claim_date']
        out_writer = csv.DictWriter(new_file, fieldnames = out_file_headers)
        out_writer.writeheader()
        for message in mbox:
            claim_date = message['date']
            # print("Channel Name:",re.search('(?<=Hi\s)(?:(.+?),)',getbody(message).decode("utf-8")).group(1))
            if (channel_name := re.search('(?<=Hi\s)(?:(.+?),)',getbody(message).decode("utf-8"))) is not None:
                channel_name = channel_name.group(1)
            else:
                channel_name = "N/A"
            # print("Video title:",re.search('(?<=Video title:\s)(?:(.+?)\\r\\n)',getbody(message).decode("utf-8")).group(1))
            if (video_title := re.search('(?<=Video title:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
                video_title = video_title.group(1)
            else:
                video_title = "N/A"
            # print("Copyrighted content:",re.search('(?<=Copyrighted content:\s)(?:(.+?)\n)',getbody(message).decode("utf-8")).group(1))
            if (copyrighted_content := re.search('(?<=Copyrighted content:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
                copyrighted_content = copyrighted_content.group(1)
            else:
                copyrighted_content = "N/A"
            # print("Claimed by:",re.search('(?<=Claimed by:\s)(?:(.+?)\n)',getbody(message).decode("utf-8")).group(1))
            if (claimed_by := re.search('(?<=Claimed by:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
                claimed_by = claimed_by.group(1)
            else:
                claimed_by = "N/A"
            # print("Claim details:",re.search('(?<=View claim details:\s)(?:(.+?)\n)',getbody(message).decode("utf-8")).group(1))
            if (claim_details := re.search('(?<=View claim details:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
                claim_details = claim_details.group(1)
            else:
                claim_details = "N/A"
            # print("Note:",re.search('(?<=Note:\s)(?:(.+?)\\r\\n\\r)',getbody(message).decode("utf-8")).group(1))
            if (claim_note := re.search('(?<=Note:\s)(?:(.+?)\r)',getbody(message).decode("utf-8"))) is not None:
                claim_note = claim_note.group(1)
            else:
                claim_note = "N/A"
            
            out_writer.writerow({'channel_name' : channel_name,'video_title' : video_title,'copyrighted_content' : copyrighted_content,'claimed_by' : claimed_by,'claim_note' : claim_note,'claim_url' : claim_details,'claim_date' : claim_date})

            total_messages +=1

if __name__ == "__main__":
    main()