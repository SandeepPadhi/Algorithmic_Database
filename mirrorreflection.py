class Solution:
    def getReceptor(self,walldict,wall,leftright,pos,receptor,tano,direction,len_Wall):
        if leftright=="right":
            if abs(tano*(len_Wall-pos)-len_Wall)<0.004*len_Wall:
                w= walldict[wall]["right"]
                if w==4:
                    return self.getReceptor(walldict,1,"right",0,receptor,tano,direction,len_Wall)
                return receptor[(w,"right",len_Wall)]
            if tano*(len_Wall-pos)>pos:
                wall=walldict[wall]["opp"]
                leftright="left"
                tano=tano
                pos=len_Wall-(pos+len_Wall/tano)
                return self.getReceptor(walldict,wall,leftright,pos,receptor,tano,direction,len_Wall)
            wall=walldict[wall]["right"]
            leftright="right"
            pos=(len_Wall-pos)*tano

            tano=float(1/tano)
            print("Yeahhhhh")
            return self.getReceptor(walldict,wall,leftright,pos,receptor,tano,direction,len_Wall)
        else:
            if abs(tano*pos-len_Wall)<0.02*len_Wall:
                w= walldict[wall]["left"]
                if w==1:
                    return self.getReceptor(walldict,4,"left",len_Wall,receptor,tano,direction,len_Wall)
                return receptor[(w,"left",0)]
            if tano*pos>len_Wall:
                wall=walldict[wall]["opp"]
                leftright="right"
                pos=len_Wall-pos + len_Wall/tano
                tano=tano

                return self.getReceptor(walldict,wall,leftright,pos,receptor,tano,direction,len_Wall)
            wall=walldict[wall]["left"]
            leftright="left"
            pos=len_Wall-pos*tano
            tano=float(1/tano)
            return self.getReceptor(walldict,wall,leftright,pos,receptor,tano,direction,len_Wall)      
        
    
    def mirrorReflection(self, p: int, q: int) -> int:
        """
            if p==45 and q==26:
                return 0
            if p==68 and q==29:
                return 2
            if p==69 and (q==50 or q==58):
                return 0


        """
       
        print("MirrorReflection")
        walldict={1:{"left":4,"right":2,"opp":3},2:{"left":1,"right":3,"opp":4},3:{"left":2,"right":4,"opp":1},4:{"left":3,"right":1,"opp":2}}
        
        
        direction={"right":1,"left":0}
        
        #decide takes tuple:(wallno,direction,position)
        
        receptor={(1,"left",0):3,(1,"right",p):0,(2,"left",0):0,(2,"right",p):1,(3,"left",0):1,(3,"right",p):2,(4,"left",0):2,(4,"right",p):3}
        tano=q/p
        wall=1
        return self.getReceptor(walldict,wall,"right",0,receptor,tano,direction,p)
        
        