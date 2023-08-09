from collections import deque
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        
        for cpdomain in cpdomains:
            # iterate over levels in domain in reverse order
            count, domain = cpdomain.split(' ')
            print("count", count, "domain", domain)
            subdomains = deque(domain.split('.'))
            print("subdomain", subdomains)
            while subdomains:
                domain = '.'.join(subdomains)
                print("domain", domain)
                counts[domain] = counts.get(domain, 0) + int(count)
                print("counts", counts)
                subdomains.popleft()
                print("subdomains", subdomains)
            
        res = []
        for domain, count in counts.items():
            res.append(f"{count} {domain}")
            
        return res