# knowledge: split()[n]
# concepts: string manipulation
# comment: easy string manipulation, use sets and split
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        for email in emails:
            local_name, domain_name = email.split("@")
            local_name = "".join(local_name.split('+')[0].split('.'))
            email = local_name + '@' + domain_name
            uniqueEmails.add(email)
        return len(uniqueEmails)