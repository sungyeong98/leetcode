class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        result=set()
        for email in emails:
            local_name,domain_name=email.split('@')
            
            local_name=''.join(local_name.split('.'))

            fixed_local_name=local_name.split('+')[0]

            result.add(fixed_local_name+'@'+domain_name)
        return len(result)