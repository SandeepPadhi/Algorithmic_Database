"""
Date:16/04/2021
1125. Smallest Sufficient Team - Leetcode Hard

The following problem is solved using Sets and backtracking
"""
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        for i in range(len(people)):
            people[i]=set(people[i])
        
        for i in range(len(people)):
            for j in range(len(people)):
                if i!=j and people[i].issubset(people[j]):
                    people[i]=set()
        
        skill_to_person={}
        
        for i in range(len(people)):
            for skill in people[i]:
                if skill not in skill_to_person:
                    skill_to_person[skill]=set()
                skill_to_person[skill].add(i)
                
        
        
        unmet_skills=set(req_skills)
        Best_Team=[]
        Team=[]
        Min_Team=100000000
        def meet_skill(skill=0):
            nonlocal unmet_skills,Best_Team,Team,Min_Team
            if not unmet_skills:
                if Min_Team>len(Team):
                    Best_Team=Team[::]
                    Min_Team=len(Team)
                return
            
            if req_skills[skill] not in unmet_skills:
                meet_skill(skill+1)
                return
            
            for person in skill_to_person[req_skills[skill]]:
                
                skill_to_add=unmet_skills.intersection(people[person])
                unmet_skills-=skill_to_add
                Team.append(person)
                meet_skill(skill+1)
                Team.pop()
                unmet_skills=unmet_skills.union(skill_to_add)
                
                    
    
        
        meet_skill()
        return Best_Team
        
        
        
        
        