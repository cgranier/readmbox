import mailbox
import re

mbox_file = "data/CLAIM.mbox"
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
    for message in mbox:
        print("Message #:", total_messages)
        # print("from   :",message['from'])
        print("date   :",message['date'])
        # print("subject:",message['subject'])
        print("Channel Name:",re.search('(?<=Hi\s)(?:(.+?),)',getbody(message).decode("utf-8")).group(1))
        # print("Video title:",re.search('(?<=Video title:\s)(?:(.+?)\\r\\n)',getbody(message).decode("utf-8")).group(1))
        if (video_title := re.search('(?<=Video title:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
            print("Video title:", video_title.group(1))
        else:
            print("message: ",getbody(message).decode("utf-8"))
            
        # print("Copyrighted content:",re.search('(?<=Copyrighted content:\s)(?:(.+?)\n)',getbody(message).decode("utf-8")).group(1))
        if (copyrighted_content := re.search('(?<=Copyrighted content:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
            print("Copyrighted content:", copyrighted_content.group(1))

        # print("Claimed by:",re.search('(?<=Claimed by:\s)(?:(.+?)\n)',getbody(message).decode("utf-8")).group(1))
        if (claimed_by := re.search('(?<=Claimed by:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
            print("Claimed by:", claimed_by.group(1))
            
        # print("Claim details:",re.search('(?<=View claim details:\s)(?:(.+?)\n)',getbody(message).decode("utf-8")).group(1))
        if (claim_details := re.search('(?<=View claim details:\s)(?:(.+?)\n)',getbody(message).decode("utf-8"))) is not None:
            print("Claim details:", claim_details.group(1))
            
        # print("Note:",re.search('(?<=Note:\s)(?:(.+?)\\r\\n\\r)',getbody(message).decode("utf-8")).group(1))
        if (claim_note := re.search('(?<=Note:\s)(?:(.+?)\\r\\n\\r)',getbody(message).decode("utf-8"))) is not None:
            print("Note:", claim_note.group(1))
        
        print("**************************************")

        total_messages +=1



if __name__ == "__main__":
    main()