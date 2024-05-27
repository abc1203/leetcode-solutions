class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        unique = set()
        for email in emails:
            name = email.split('@')
            local, domain = name[0], name[1]

            local = ''.join(local.split('.'))
            local = (local.split('+'))[0]
            unique.add((local, domain))
        return len(unique)
        
