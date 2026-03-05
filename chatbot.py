def get_response(user_input):

    knowledge = {
        "what is sql injection": "SQL Injection is a vulnerability where attackers manipulate database queries through unsanitized input.",
        "what is xss": "Cross Site Scripting (XSS) allows attackers to inject malicious scripts into web pages viewed by other users.",
        "what is malware": "Malware is malicious software designed to damage, disrupt, or gain unauthorized access to systems.",
        "what is ddos": "DDoS is a Distributed Denial of Service attack that floods a server with traffic to make it unavailable."
    }

    if user_input == "help":
        return """Available commands:
help  - show commands
clear - clear terminal
exit  - quit chatbot

Ask cybersecurity questions like:
- what is sql injection
- what is xss
- what is malware
"""

    if user_input in knowledge:
        return knowledge[user_input]

    return "I don't know that yet. Try asking about common cybersecurity topics."
