clean_cmd = re.sub(r'\b(com(and|mand)?)\b', 'com', clean_cmd)

        parts = re.split(r'\b(type|write|saying|message|content|with body)\b', clean_cmd)
        recip_part = parts[0].strip()

        recip_part = re.sub(r'^(update\s+to|to|send\s+to|and\s+update\s+to)\s*', '', recip_part).strip()

        if len(parts) > 1:
            body = parts[-1].strip()

        if recip_part:
            c = recip_part.replace(" at ", "@").replace(" dot ", ".").replace(" ", "")
            c = re.sub(r'[^a-zA-Z0-9@._%-]', '', c)
            to = c if "@" in c else f"{c}@gmail.com"

        base = "https://mail.google.com/mail/u/0/?view=cm&fs=1"
        params = urllib.parse.urlencode({"to": to, "body": body})
        target = f"{base}&{params}"
        msg = f"Drafting email to {to}"
