import pygame

class Intro():
    def __init__(self, game):
        self.game = game
        self.number = 1
        self.timer = 0
        self.bg1 = pygame.image.load("assets/frames_intro/frame (1).jpg")
        self.bg2 = pygame.image.load("assets/frames_intro/frame (2).jpg")
        self.bg3 = pygame.image.load("assets/frames_intro/frame (3).jpg")
        self.bg4 = pygame.image.load("assets/frames_intro/frame (4).jpg")
        self.bg5 = pygame.image.load("assets/frames_intro/frame (5).jpg")
        self.bg6 = pygame.image.load("assets/frames_intro/frame (6).jpg")
        self.bg7 = pygame.image.load("assets/frames_intro/frame (7).jpg")
        self.bg8 = pygame.image.load("assets/frames_intro/frame (8).jpg")
        self.bg9 = pygame.image.load("assets/frames_intro/frame (9).jpg")
        self.bg10 = pygame.image.load("assets/frames_intro/frame (10).jpg")
        self.bg11 = pygame.image.load("assets/frames_intro/frame (11).jpg")
        self.bg12 = pygame.image.load("assets/frames_intro/frame (12).jpg")
        self.bg13 = pygame.image.load("assets/frames_intro/frame (13).jpg")
        self.bg14 = pygame.image.load("assets/frames_intro/frame (14).jpg")
        self.bg15 = pygame.image.load("assets/frames_intro/frame (15).jpg")
        self.bg16 = pygame.image.load("assets/frames_intro/frame (16).jpg")
        self.bg17 = pygame.image.load("assets/frames_intro/frame (17).jpg")
        self.bg18 = pygame.image.load("assets/frames_intro/frame (18).jpg")
        self.bg19 = pygame.image.load("assets/frames_intro/frame (19).jpg")
        self.bg20 = pygame.image.load("assets/frames_intro/frame (20).jpg")
        self.bg21 = pygame.image.load("assets/frames_intro/frame (21).jpg")
        self.bg22 = pygame.image.load("assets/frames_intro/frame (22).jpg")
        self.bg23 = pygame.image.load("assets/frames_intro/frame (23).jpg")
        self.bg24 = pygame.image.load("assets/frames_intro/frame (24).jpg")
        self.bg25 = pygame.image.load("assets/frames_intro/frame (25).jpg")
        self.bg26 = pygame.image.load("assets/frames_intro/frame (26).jpg")
        self.bg27 = pygame.image.load("assets/frames_intro/frame (27).jpg")
        self.bg28 = pygame.image.load("assets/frames_intro/frame (28).jpg")
        self.bg29 = pygame.image.load("assets/frames_intro/frame (29).jpg")
        self.bg30 = pygame.image.load("assets/frames_intro/frame (30).jpg")
        self.bg31 = pygame.image.load("assets/frames_intro/frame (31).jpg")
        self.bg32 = pygame.image.load("assets/frames_intro/frame (32).jpg")
        self.bg33 = pygame.image.load("assets/frames_intro/frame (33).jpg")
        self.bg34 = pygame.image.load("assets/frames_intro/frame (34).jpg")
        self.bg35 = pygame.image.load("assets/frames_intro/frame (35).jpg")
        self.bg36 = pygame.image.load("assets/frames_intro/frame (36).jpg")
        self.bg37 = pygame.image.load("assets/frames_intro/frame (37).jpg")
        self.bg38 = pygame.image.load("assets/frames_intro/frame (38).jpg")
        self.bg39 = pygame.image.load("assets/frames_intro/frame (39).jpg")
        self.bg40 = pygame.image.load("assets/frames_intro/frame (40).jpg")
        self.bg41 = pygame.image.load("assets/frames_intro/frame (41).jpg")
        self.bg42 = pygame.image.load("assets/frames_intro/frame (42).jpg")
        self.bg43 = pygame.image.load("assets/frames_intro/frame (43).jpg")
        self.bg44 = pygame.image.load("assets/frames_intro/frame (44).jpg")
        self.bg45 = pygame.image.load("assets/frames_intro/frame (45).jpg")
        self.bg46 = pygame.image.load("assets/frames_intro/frame (46).jpg")
        self.bg47 = pygame.image.load("assets/frames_intro/frame (47).jpg")
        self.bg48 = pygame.image.load("assets/frames_intro/frame (48).jpg")
        self.bg49 = pygame.image.load("assets/frames_intro/frame (49).jpg")
        self.bg50 = pygame.image.load("assets/frames_intro/frame (50).jpg")
        self.bg51 = pygame.image.load("assets/frames_intro/frame (51).jpg")
        self.bg52 = pygame.image.load("assets/frames_intro/frame (52).jpg")
        self.bg53 = pygame.image.load("assets/frames_intro/frame (53).jpg")
        self.bg54 = pygame.image.load("assets/frames_intro/frame (54).jpg")
        self.bg55 = pygame.image.load("assets/frames_intro/frame (55).jpg")
        self.bg56 = pygame.image.load("assets/frames_intro/frame (56).jpg")
        self.bg57 = pygame.image.load("assets/frames_intro/frame (57).jpg")
        self.bg58 = pygame.image.load("assets/frames_intro/frame (58).jpg")
        self.bg59 = pygame.image.load("assets/frames_intro/frame (59).jpg")
        self.bg60 = pygame.image.load("assets/frames_intro/frame (60).jpg")
        self.bg61 = pygame.image.load("assets/frames_intro/frame (61).jpg")
        self.bg62 = pygame.image.load("assets/frames_intro/frame (62).jpg")
        self.bg63 = pygame.image.load("assets/frames_intro/frame (63).jpg")
        self.bg64 = pygame.image.load("assets/frames_intro/frame (64).jpg")
        self.bg65 = pygame.image.load("assets/frames_intro/frame (65).jpg")
        self.bg66 = pygame.image.load("assets/frames_intro/frame (66).jpg")
        self.bg67 = pygame.image.load("assets/frames_intro/frame (67).jpg")
        self.bg68 = pygame.image.load("assets/frames_intro/frame (68).jpg")
        self.bg69 = pygame.image.load("assets/frames_intro/frame (69).jpg")
        self.bg70 = pygame.image.load("assets/frames_intro/frame (70).jpg")
        self.bg71 = pygame.image.load("assets/frames_intro/frame (71).jpg")
        self.bg72 = pygame.image.load("assets/frames_intro/frame (72).jpg")
        self.bg73 = pygame.image.load("assets/frames_intro/frame (73).jpg")
        self.bg74 = pygame.image.load("assets/frames_intro/frame (74).jpg")
        self.bg75 = pygame.image.load("assets/frames_intro/frame (75).jpg")
        self.bg76 = pygame.image.load("assets/frames_intro/frame (76).jpg")
        self.bg77 = pygame.image.load("assets/frames_intro/frame (77).jpg")
        self.bg78 = pygame.image.load("assets/frames_intro/frame (78).jpg")
        self.bg79 = pygame.image.load("assets/frames_intro/frame (79).jpg")
        self.bg80 = pygame.image.load("assets/frames_intro/frame (80).jpg")
        self.bg81 = pygame.image.load("assets/frames_intro/frame (81).jpg")
        self.bg82 = pygame.image.load("assets/frames_intro/frame (82).jpg")
        self.bg83 = pygame.image.load("assets/frames_intro/frame (83).jpg")
        self.bg84 = pygame.image.load("assets/frames_intro/frame (84).jpg")
        self.bg85 = pygame.image.load("assets/frames_intro/frame (85).jpg")
        self.bg86 = pygame.image.load("assets/frames_intro/frame (86).jpg")
        self.bg87 = pygame.image.load("assets/frames_intro/frame (87).jpg")
        self.bg88 = pygame.image.load("assets/frames_intro/frame (88).jpg")
        self.bg89 = pygame.image.load("assets/frames_intro/frame (89).jpg")
        self.bg90 = pygame.image.load("assets/frames_intro/frame (90).jpg")
        self.bg91 = pygame.image.load("assets/frames_intro/frame (91).jpg")
        self.bg92 = pygame.image.load("assets/frames_intro/frame (92).jpg")
        self.bg93 = pygame.image.load("assets/frames_intro/frame (93).jpg")
        self.bg94 = pygame.image.load("assets/frames_intro/frame (94).jpg")
        self.bg95 = pygame.image.load("assets/frames_intro/frame (95).jpg")
        self.bg96 = pygame.image.load("assets/frames_intro/frame (96).jpg")
        self.bg97 = pygame.image.load("assets/frames_intro/frame (97).jpg")
        self.bg98 = pygame.image.load("assets/frames_intro/frame (98).jpg")
        self.bg99 = pygame.image.load("assets/frames_intro/frame (99).jpg")
        self.bg100 = pygame.image.load("assets/frames_intro/frame (100).jpg")
        self.bg101 = pygame.image.load("assets/frames_intro/frame (101).jpg")
        self.bg102 = pygame.image.load("assets/frames_intro/frame (102).jpg")
        self.bg103 = pygame.image.load("assets/frames_intro/frame (103).jpg")
        self.bg104 = pygame.image.load("assets/frames_intro/frame (104).jpg")
        self.bg105 = pygame.image.load("assets/frames_intro/frame (105).jpg")
        self.bg106 = pygame.image.load("assets/frames_intro/frame (106).jpg")
        self.bg107 = pygame.image.load("assets/frames_intro/frame (107).jpg")
        self.bg108 = pygame.image.load("assets/frames_intro/frame (108).jpg")
        self.bg109 = pygame.image.load("assets/frames_intro/frame (109).jpg")
        self.bg110 = pygame.image.load("assets/frames_intro/frame (110).jpg")
        self.bg111 = pygame.image.load("assets/frames_intro/frame (111).jpg")
        self.bg112 = pygame.image.load("assets/frames_intro/frame (112).jpg")
        self.bg113 = pygame.image.load("assets/frames_intro/frame (113).jpg")
        self.bg114 = pygame.image.load("assets/frames_intro/frame (114).jpg")
        self.bg115 = pygame.image.load("assets/frames_intro/frame (115).jpg")
        self.bg116 = pygame.image.load("assets/frames_intro/frame (116).jpg")
        self.bg117 = pygame.image.load("assets/frames_intro/frame (117).jpg")
        self.bg118 = pygame.image.load("assets/frames_intro/frame (118).jpg")
        self.bg119 = pygame.image.load("assets/frames_intro/frame (119).jpg")
        self.bg120 = pygame.image.load("assets/frames_intro/frame (120).jpg")
        self.bg121 = pygame.image.load("assets/frames_intro/frame (121).jpg")
        self.bg122 = pygame.image.load("assets/frames_intro/frame (122).jpg")
        self.bg123 = pygame.image.load("assets/frames_intro/frame (123).jpg")
        self.bg124 = pygame.image.load("assets/frames_intro/frame (124).jpg")
        self.bg125 = pygame.image.load("assets/frames_intro/frame (125).jpg")
        self.bg126 = pygame.image.load("assets/frames_intro/frame (126).jpg")
        self.bg127 = pygame.image.load("assets/frames_intro/frame (127).jpg")
        self.bg128 = pygame.image.load("assets/frames_intro/frame (128).jpg")
        self.bg129 = pygame.image.load("assets/frames_intro/frame (129).jpg")
        self.bg130 = pygame.image.load("assets/frames_intro/frame (130).jpg")
        self.bg131 = pygame.image.load("assets/frames_intro/frame (131).jpg")
        self.bg132 = pygame.image.load("assets/frames_intro/frame (132).jpg")
        self.bg133 = pygame.image.load("assets/frames_intro/frame (133).jpg")
        self.bg134 = pygame.image.load("assets/frames_intro/frame (134).jpg")
        self.bg135 = pygame.image.load("assets/frames_intro/frame (135).jpg")
        self.bg136 = pygame.image.load("assets/frames_intro/frame (136).jpg")
        self.bg137 = pygame.image.load("assets/frames_intro/frame (137).jpg")
        self.bg138 = pygame.image.load("assets/frames_intro/frame (138).jpg")
        self.bg139 = pygame.image.load("assets/frames_intro/frame (139).jpg")
        self.bg140 = pygame.image.load("assets/frames_intro/frame (140).jpg")
        self.bg141 = pygame.image.load("assets/frames_intro/frame (141).jpg")
        self.bg142 = pygame.image.load("assets/frames_intro/frame (142).jpg")
        self.bg143 = pygame.image.load("assets/frames_intro/frame (143).jpg")
        self.bg144 = pygame.image.load("assets/frames_intro/frame (144).jpg")
        self.bg145 = pygame.image.load("assets/frames_intro/frame (145).jpg")
        self.bg146 = pygame.image.load("assets/frames_intro/frame (146).jpg")
        self.bg147 = pygame.image.load("assets/frames_intro/frame (147).jpg")
        self.bg148 = pygame.image.load("assets/frames_intro/frame (148).jpg")
        self.bg149 = pygame.image.load("assets/frames_intro/frame (149).jpg")
        self.bg150 = pygame.image.load("assets/frames_intro/frame (150).jpg")
        self.bg151 = pygame.image.load("assets/frames_intro/frame (151).jpg")
        self.bg152 = pygame.image.load("assets/frames_intro/frame (152).jpg")
        self.bg153 = pygame.image.load("assets/frames_intro/frame (153).jpg")
        self.bg154 = pygame.image.load("assets/frames_intro/frame (154).jpg")
        self.bg155 = pygame.image.load("assets/frames_intro/frame (155).jpg")
        self.bg156 = pygame.image.load("assets/frames_intro/frame (156).jpg")
        self.bg157 = pygame.image.load("assets/frames_intro/frame (157).jpg")
        self.bg158 = pygame.image.load("assets/frames_intro/frame (158).jpg")
        self.bg159 = pygame.image.load("assets/frames_intro/frame (159).jpg")
        self.bg160 = pygame.image.load("assets/frames_intro/frame (160).jpg")
        self.bg161 = pygame.image.load("assets/frames_intro/frame (161).jpg")
        self.bg162 = pygame.image.load("assets/frames_intro/frame (162).jpg")
        self.bg163 = pygame.image.load("assets/frames_intro/frame (163).jpg")
        self.bg164 = pygame.image.load("assets/frames_intro/frame (164).jpg")
        self.bg165 = pygame.image.load("assets/frames_intro/frame (165).jpg")
        self.bg166 = pygame.image.load("assets/frames_intro/frame (166).jpg")
        self.bg167 = pygame.image.load("assets/frames_intro/frame (167).jpg")
        self.bg168 = pygame.image.load("assets/frames_intro/frame (168).jpg")
        self.bg169 = pygame.image.load("assets/frames_intro/frame (169).jpg")
        self.bg170 = pygame.image.load("assets/frames_intro/frame (170).jpg")
        self.bg171 = pygame.image.load("assets/frames_intro/frame (171).jpg")
        self.bg172 = pygame.image.load("assets/frames_intro/frame (172).jpg")
        self.bg173 = pygame.image.load("assets/frames_intro/frame (173).jpg")
        self.bg174 = pygame.image.load("assets/frames_intro/frame (174).jpg")
        self.bg175 = pygame.image.load("assets/frames_intro/frame (175).jpg")
        self.bg176 = pygame.image.load("assets/frames_intro/frame (176).jpg")
        self.bg177 = pygame.image.load("assets/frames_intro/frame (177).jpg")
        self.bg178 = pygame.image.load("assets/frames_intro/frame (178).jpg")
        self.bg179 = pygame.image.load("assets/frames_intro/frame (179).jpg")
        self.bg180 = pygame.image.load("assets/frames_intro/frame (180).jpg")
        self.bg181 = pygame.image.load("assets/frames_intro/frame (181).jpg")
        self.bg182 = pygame.image.load("assets/frames_intro/frame (182).jpg")
        self.bg183 = pygame.image.load("assets/frames_intro/frame (183).jpg")
        self.bg184 = pygame.image.load("assets/frames_intro/frame (184).jpg")
        self.bg185 = pygame.image.load("assets/frames_intro/frame (185).jpg")
        self.bg186 = pygame.image.load("assets/frames_intro/frame (186).jpg")
        self.bg187 = pygame.image.load("assets/frames_intro/frame (187).jpg")
        self.bg188 = pygame.image.load("assets/frames_intro/frame (188).jpg")
        self.bg189 = pygame.image.load("assets/frames_intro/frame (189).jpg")
        self.bg190 = pygame.image.load("assets/frames_intro/frame (190).jpg")
        self.bg191 = pygame.image.load("assets/frames_intro/frame (191).jpg")
        self.bg192 = pygame.image.load("assets/frames_intro/frame (192).jpg")
        self.bg193 = pygame.image.load("assets/frames_intro/frame (193).jpg")
        self.bg194 = pygame.image.load("assets/frames_intro/frame (194).jpg")
        self.bg195 = pygame.image.load("assets/frames_intro/frame (195).jpg")
        self.bg196 = pygame.image.load("assets/frames_intro/frame (196).jpg")
        self.bg197 = pygame.image.load("assets/frames_intro/frame (197).jpg")
        self.bg198 = pygame.image.load("assets/frames_intro/frame (198).jpg")
        self.bg199 = pygame.image.load("assets/frames_intro/frame (199).jpg")
        self.bg200 = pygame.image.load("assets/frames_intro/frame (200).jpg")
        self.bg201 = pygame.image.load("assets/frames_intro/frame (201).jpg")
        self.bg202 = pygame.image.load("assets/frames_intro/frame (202).jpg")
        self.bg203 = pygame.image.load("assets/frames_intro/frame (203).jpg")
        self.bg204 = pygame.image.load("assets/frames_intro/frame (204).jpg")
        self.bg205 = pygame.image.load("assets/frames_intro/frame (205).jpg")
        self.bg206 = pygame.image.load("assets/frames_intro/frame (206).jpg")
        self.bg207 = pygame.image.load("assets/frames_intro/frame (207).jpg")
        self.bg208 = pygame.image.load("assets/frames_intro/frame (208).jpg")
        self.bg209 = pygame.image.load("assets/frames_intro/frame (209).jpg")
        self.bg210 = pygame.image.load("assets/frames_intro/frame (210).jpg")
        self.bg211 = pygame.image.load("assets/frames_intro/frame (211).jpg")
        self.bg212 = pygame.image.load("assets/frames_intro/frame (212).jpg")
        self.bg213 = pygame.image.load("assets/frames_intro/frame (213).jpg")
        self.bg214 = pygame.image.load("assets/frames_intro/frame (214).jpg")
        self.bg215 = pygame.image.load("assets/frames_intro/frame (215).jpg")
        self.bg216 = pygame.image.load("assets/frames_intro/frame (216).jpg")
        self.bg217 = pygame.image.load("assets/frames_intro/frame (217).jpg")
        self.bg218 = pygame.image.load("assets/frames_intro/frame (218).jpg")
        self.bg219 = pygame.image.load("assets/frames_intro/frame (219).jpg")
        self.bg220 = pygame.image.load("assets/frames_intro/frame (220).jpg")
        self.bg221 = pygame.image.load("assets/frames_intro/frame (221).jpg")
        self.bg222 = pygame.image.load("assets/frames_intro/frame (222).jpg")
        self.bg223 = pygame.image.load("assets/frames_intro/frame (223).jpg")
        self.bg224 = pygame.image.load("assets/frames_intro/frame (224).jpg")
        self.bg225 = pygame.image.load("assets/frames_intro/frame (225).jpg")
        self.bg226 = pygame.image.load("assets/frames_intro/frame (226).jpg")
        self.bg227 = pygame.image.load("assets/frames_intro/frame (227).jpg")
        self.bg228 = pygame.image.load("assets/frames_intro/frame (228).jpg")
        self.bg229 = pygame.image.load("assets/frames_intro/frame (229).jpg")
        self.bg230 = pygame.image.load("assets/frames_intro/frame (230).jpg")
        self.bg231 = pygame.image.load("assets/frames_intro/frame (231).jpg")
        self.bg232 = pygame.image.load("assets/frames_intro/frame (232).jpg")
        self.bg233 = pygame.image.load("assets/frames_intro/frame (233).jpg")
        self.bg234 = pygame.image.load("assets/frames_intro/frame (234).jpg")
        self.bg235 = pygame.image.load("assets/frames_intro/frame (235).jpg")
        self.bg236 = pygame.image.load("assets/frames_intro/frame (236).jpg")
        self.bg237 = pygame.image.load("assets/frames_intro/frame (237).jpg")
        self.bg238 = pygame.image.load("assets/frames_intro/frame (238).jpg")
        self.bg239 = pygame.image.load("assets/frames_intro/frame (239).jpg")
        self.bg240 = pygame.image.load("assets/frames_intro/frame (240).jpg")
        self.bg241 = pygame.image.load("assets/frames_intro/frame (241).jpg")
        self.bg1 = pygame.transform.scale(self.bg1, (1440,809))
        self.bg2 = pygame.transform.scale(self.bg2, (1440,809))
        self.bg3 = pygame.transform.scale(self.bg3, (1440,809))
        self.bg4 = pygame.transform.scale(self.bg4, (1440,809))
        self.bg5 = pygame.transform.scale(self.bg5, (1440,809))
        self.bg6 = pygame.transform.scale(self.bg6, (1440,809))
        self.bg7 = pygame.transform.scale(self.bg7, (1440,809))
        self.bg8 = pygame.transform.scale(self.bg8, (1440,809))
        self.bg9 = pygame.transform.scale(self.bg9, (1440,809))
        self.bg10 = pygame.transform.scale(self.bg10, (1440,809))
        self.bg11 = pygame.transform.scale(self.bg11, (1440,809))
        self.bg12 = pygame.transform.scale(self.bg12, (1440,809))
        self.bg13 = pygame.transform.scale(self.bg13, (1440,809))
        self.bg14 = pygame.transform.scale(self.bg14, (1440,809))
        self.bg15 = pygame.transform.scale(self.bg15, (1440,809))
        self.bg16 = pygame.transform.scale(self.bg16, (1440,809))
        self.bg17 = pygame.transform.scale(self.bg17, (1440,809))
        self.bg18 = pygame.transform.scale(self.bg18, (1440,809))
        self.bg19 = pygame.transform.scale(self.bg19, (1440,809))
        self.bg20 = pygame.transform.scale(self.bg20, (1440,809))
        self.bg21 = pygame.transform.scale(self.bg21, (1440,809))
        self.bg22 = pygame.transform.scale(self.bg22, (1440,809))
        self.bg23 = pygame.transform.scale(self.bg23, (1440,809))
        self.bg24 = pygame.transform.scale(self.bg24, (1440,809))
        self.bg25 = pygame.transform.scale(self.bg25, (1440,809))
        self.bg26 = pygame.transform.scale(self.bg26, (1440,809))
        self.bg27 = pygame.transform.scale(self.bg27, (1440,809))
        self.bg28 = pygame.transform.scale(self.bg28, (1440,809))
        self.bg29 = pygame.transform.scale(self.bg29, (1440,809))
        self.bg30 = pygame.transform.scale(self.bg30, (1440,809))
        self.bg31 = pygame.transform.scale(self.bg31, (1440,809))
        self.bg32 = pygame.transform.scale(self.bg32, (1440,809))
        self.bg33 = pygame.transform.scale(self.bg33, (1440,809))
        self.bg34 = pygame.transform.scale(self.bg34, (1440,809))
        self.bg35 = pygame.transform.scale(self.bg35, (1440,809))
        self.bg36 = pygame.transform.scale(self.bg36, (1440,809))
        self.bg37 = pygame.transform.scale(self.bg37, (1440,809))
        self.bg38 = pygame.transform.scale(self.bg38, (1440,809))
        self.bg39 = pygame.transform.scale(self.bg39, (1440,809))
        self.bg40 = pygame.transform.scale(self.bg40, (1440,809))
        self.bg41 = pygame.transform.scale(self.bg41, (1440,809))
        self.bg42 = pygame.transform.scale(self.bg42, (1440,809))
        self.bg43 = pygame.transform.scale(self.bg43, (1440,809))
        self.bg44 = pygame.transform.scale(self.bg44, (1440,809))
        self.bg45 = pygame.transform.scale(self.bg45, (1440,809))
        self.bg46 = pygame.transform.scale(self.bg46, (1440,809))
        self.bg47 = pygame.transform.scale(self.bg47, (1440,809))
        self.bg48 = pygame.transform.scale(self.bg48, (1440,809))
        self.bg49 = pygame.transform.scale(self.bg49, (1440,809))
        self.bg50 = pygame.transform.scale(self.bg50, (1440,809))
        self.bg51 = pygame.transform.scale(self.bg51, (1440,809))
        self.bg52 = pygame.transform.scale(self.bg52, (1440,809))
        self.bg53 = pygame.transform.scale(self.bg53, (1440,809))
        self.bg54 = pygame.transform.scale(self.bg54, (1440,809))
        self.bg55 = pygame.transform.scale(self.bg55, (1440,809))
        self.bg56 = pygame.transform.scale(self.bg56, (1440,809))
        self.bg57 = pygame.transform.scale(self.bg57, (1440,809))
        self.bg58 = pygame.transform.scale(self.bg58, (1440,809))
        self.bg59 = pygame.transform.scale(self.bg59, (1440,809))
        self.bg60 = pygame.transform.scale(self.bg60, (1440,809))
        self.bg61 = pygame.transform.scale(self.bg61, (1440,809))
        self.bg62 = pygame.transform.scale(self.bg62, (1440,809))
        self.bg63 = pygame.transform.scale(self.bg63, (1440,809))
        self.bg64 = pygame.transform.scale(self.bg64, (1440,809))
        self.bg65 = pygame.transform.scale(self.bg65, (1440,809))
        self.bg66 = pygame.transform.scale(self.bg66, (1440,809))
        self.bg67 = pygame.transform.scale(self.bg67, (1440,809))
        self.bg68 = pygame.transform.scale(self.bg68, (1440,809))
        self.bg69 = pygame.transform.scale(self.bg69, (1440,809))
        self.bg70 = pygame.transform.scale(self.bg70, (1440,809))
        self.bg71 = pygame.transform.scale(self.bg71, (1440,809))
        self.bg72 = pygame.transform.scale(self.bg72, (1440,809))
        self.bg73 = pygame.transform.scale(self.bg73, (1440,809))
        self.bg74 = pygame.transform.scale(self.bg74, (1440,809))
        self.bg75 = pygame.transform.scale(self.bg75, (1440,809))
        self.bg76 = pygame.transform.scale(self.bg76, (1440,809))
        self.bg77 = pygame.transform.scale(self.bg77, (1440,809))
        self.bg78 = pygame.transform.scale(self.bg78, (1440,809))
        self.bg79 = pygame.transform.scale(self.bg79, (1440,809))
        self.bg80 = pygame.transform.scale(self.bg80, (1440,809))
        self.bg81 = pygame.transform.scale(self.bg81, (1440,809))
        self.bg82 = pygame.transform.scale(self.bg82, (1440,809))
        self.bg83 = pygame.transform.scale(self.bg83, (1440,809))
        self.bg84 = pygame.transform.scale(self.bg84, (1440,809))
        self.bg85 = pygame.transform.scale(self.bg85, (1440,809))
        self.bg86 = pygame.transform.scale(self.bg86, (1440,809))
        self.bg87 = pygame.transform.scale(self.bg87, (1440,809))
        self.bg88 = pygame.transform.scale(self.bg88, (1440,809))
        self.bg89 = pygame.transform.scale(self.bg89, (1440,809))
        self.bg90 = pygame.transform.scale(self.bg90, (1440,809))
        self.bg91 = pygame.transform.scale(self.bg91, (1440,809))
        self.bg92 = pygame.transform.scale(self.bg92, (1440,809))
        self.bg93 = pygame.transform.scale(self.bg93, (1440,809))
        self.bg94 = pygame.transform.scale(self.bg94, (1440,809))
        self.bg95 = pygame.transform.scale(self.bg95, (1440,809))
        self.bg96 = pygame.transform.scale(self.bg96, (1440,809))
        self.bg97 = pygame.transform.scale(self.bg97, (1440,809))
        self.bg98 = pygame.transform.scale(self.bg98, (1440,809))
        self.bg99 = pygame.transform.scale(self.bg99, (1440,809))
        self.bg100= pygame.transform.scale(self.bg100, (1440,809))
        self.bg101= pygame.transform.scale(self.bg101, (1440,809))
        self.bg102= pygame.transform.scale(self.bg102, (1440,809))
        self.bg103= pygame.transform.scale(self.bg103, (1440,809))
        self.bg104= pygame.transform.scale(self.bg104, (1440,809))
        self.bg105= pygame.transform.scale(self.bg105, (1440,809))
        self.bg106= pygame.transform.scale(self.bg106, (1440,809))
        self.bg107= pygame.transform.scale(self.bg107, (1440,809))
        self.bg108= pygame.transform.scale(self.bg108, (1440,809))
        self.bg109= pygame.transform.scale(self.bg109, (1440,809))
        self.bg110= pygame.transform.scale(self.bg110, (1440,809))
        self.bg111= pygame.transform.scale(self.bg111, (1440,809))
        self.bg112= pygame.transform.scale(self.bg112, (1440,809))
        self.bg113= pygame.transform.scale(self.bg113, (1440,809))
        self.bg114= pygame.transform.scale(self.bg114, (1440,809))
        self.bg115= pygame.transform.scale(self.bg115, (1440,809))
        self.bg116= pygame.transform.scale(self.bg116, (1440,809))
        self.bg117= pygame.transform.scale(self.bg117, (1440,809))
        self.bg118= pygame.transform.scale(self.bg118, (1440,809))
        self.bg119= pygame.transform.scale(self.bg119, (1440,809))
        self.bg120= pygame.transform.scale(self.bg120, (1440,809))
        self.bg121= pygame.transform.scale(self.bg121, (1440,809))
        self.bg122= pygame.transform.scale(self.bg122, (1440,809))
        self.bg123= pygame.transform.scale(self.bg123, (1440,809))
        self.bg124= pygame.transform.scale(self.bg124, (1440,809))
        self.bg125= pygame.transform.scale(self.bg125, (1440,809))
        self.bg126= pygame.transform.scale(self.bg126, (1440,809))
        self.bg127= pygame.transform.scale(self.bg127, (1440,809))
        self.bg128= pygame.transform.scale(self.bg128, (1440,809))
        self.bg129= pygame.transform.scale(self.bg129, (1440,809))
        self.bg130= pygame.transform.scale(self.bg130, (1440,809))
        self.bg131= pygame.transform.scale(self.bg131, (1440,809))
        self.bg132= pygame.transform.scale(self.bg132, (1440,809))
        self.bg133= pygame.transform.scale(self.bg133, (1440,809))
        self.bg134= pygame.transform.scale(self.bg134, (1440,809))
        self.bg135= pygame.transform.scale(self.bg135, (1440,809))
        self.bg136= pygame.transform.scale(self.bg136, (1440,809))
        self.bg137= pygame.transform.scale(self.bg137, (1440,809))
        self.bg138= pygame.transform.scale(self.bg138, (1440,809))
        self.bg139= pygame.transform.scale(self.bg139, (1440,809))
        self.bg140= pygame.transform.scale(self.bg140, (1440,809))
        self.bg141= pygame.transform.scale(self.bg141, (1440,809))
        self.bg142= pygame.transform.scale(self.bg142, (1440,809))
        self.bg143= pygame.transform.scale(self.bg143, (1440,809))
        self.bg144= pygame.transform.scale(self.bg144, (1440,809))
        self.bg145= pygame.transform.scale(self.bg145, (1440,809))
        self.bg146= pygame.transform.scale(self.bg146, (1440,809))
        self.bg147= pygame.transform.scale(self.bg147, (1440,809))
        self.bg148= pygame.transform.scale(self.bg148, (1440,809))
        self.bg149= pygame.transform.scale(self.bg149, (1440,809))
        self.bg150= pygame.transform.scale(self.bg150, (1440,809))
        self.bg151= pygame.transform.scale(self.bg151, (1440,809))
        self.bg152= pygame.transform.scale(self.bg152, (1440,809))
        self.bg153= pygame.transform.scale(self.bg153, (1440,809))
        self.bg154= pygame.transform.scale(self.bg154, (1440,809))
        self.bg155= pygame.transform.scale(self.bg155, (1440,809))
        self.bg156= pygame.transform.scale(self.bg156, (1440,809))
        self.bg157= pygame.transform.scale(self.bg157, (1440,809))
        self.bg158= pygame.transform.scale(self.bg158, (1440,809))
        self.bg159= pygame.transform.scale(self.bg159, (1440,809))
        self.bg160= pygame.transform.scale(self.bg160, (1440,809))
        self.bg161= pygame.transform.scale(self.bg161, (1440,809))
        self.bg162= pygame.transform.scale(self.bg162, (1440,809))
        self.bg163= pygame.transform.scale(self.bg163, (1440,809))
        self.bg164= pygame.transform.scale(self.bg164, (1440,809))
        self.bg165= pygame.transform.scale(self.bg165, (1440,809))
        self.bg166= pygame.transform.scale(self.bg166, (1440,809))
        self.bg167= pygame.transform.scale(self.bg167, (1440,809))
        self.bg168= pygame.transform.scale(self.bg168, (1440,809))
        self.bg169= pygame.transform.scale(self.bg169, (1440,809))
        self.bg170= pygame.transform.scale(self.bg170, (1440,809))
        self.bg171= pygame.transform.scale(self.bg171, (1440,809))
        self.bg172= pygame.transform.scale(self.bg172, (1440,809))
        self.bg173= pygame.transform.scale(self.bg173, (1440,809))
        self.bg174= pygame.transform.scale(self.bg174, (1440,809))
        self.bg175= pygame.transform.scale(self.bg175, (1440,809))
        self.bg176= pygame.transform.scale(self.bg176, (1440,809))
        self.bg177= pygame.transform.scale(self.bg177, (1440,809))
        self.bg178= pygame.transform.scale(self.bg178, (1440,809))
        self.bg179= pygame.transform.scale(self.bg179, (1440,809))
        self.bg180= pygame.transform.scale(self.bg180, (1440,809))
        self.bg181= pygame.transform.scale(self.bg181, (1440,809))
        self.bg182= pygame.transform.scale(self.bg182, (1440,809))
        self.bg183= pygame.transform.scale(self.bg183, (1440,809))
        self.bg184= pygame.transform.scale(self.bg184, (1440,809))
        self.bg185= pygame.transform.scale(self.bg185, (1440,809))
        self.bg186= pygame.transform.scale(self.bg186, (1440,809))
        self.bg187= pygame.transform.scale(self.bg187, (1440,809))
        self.bg188= pygame.transform.scale(self.bg188, (1440,809))
        self.bg189= pygame.transform.scale(self.bg189, (1440,809))
        self.bg190= pygame.transform.scale(self.bg190, (1440,809))
        self.bg191= pygame.transform.scale(self.bg191, (1440,809))
        self.bg192= pygame.transform.scale(self.bg192, (1440,809))
        self.bg193= pygame.transform.scale(self.bg193, (1440,809))
        self.bg194= pygame.transform.scale(self.bg194, (1440,809))
        self.bg195= pygame.transform.scale(self.bg195, (1440,809))
        self.bg196= pygame.transform.scale(self.bg196, (1440,809))
        self.bg197= pygame.transform.scale(self.bg197, (1440,809))
        self.bg198= pygame.transform.scale(self.bg198, (1440,809))
        self.bg199= pygame.transform.scale(self.bg199, (1440,809))
        self.bg200= pygame.transform.scale(self.bg200, (1440,809))
        self.bg201= pygame.transform.scale(self.bg201, (1440,809))
        self.bg202= pygame.transform.scale(self.bg202, (1440,809))
        self.bg203= pygame.transform.scale(self.bg203, (1440,809))
        self.bg204= pygame.transform.scale(self.bg204, (1440,809))
        self.bg205= pygame.transform.scale(self.bg205, (1440,809))
        self.bg206= pygame.transform.scale(self.bg206, (1440,809))
        self.bg207= pygame.transform.scale(self.bg207, (1440,809))
        self.bg208= pygame.transform.scale(self.bg208, (1440,809))
        self.bg209= pygame.transform.scale(self.bg209, (1440,809))
        self.bg210= pygame.transform.scale(self.bg210, (1440,809))
        self.bg211= pygame.transform.scale(self.bg211, (1440,809))
        self.bg212= pygame.transform.scale(self.bg212, (1440,809))
        self.bg213= pygame.transform.scale(self.bg213, (1440,809))
        self.bg214= pygame.transform.scale(self.bg214, (1440,809))
        self.bg215= pygame.transform.scale(self.bg215, (1440,809))
        self.bg216= pygame.transform.scale(self.bg216, (1440,809))
        self.bg217= pygame.transform.scale(self.bg217, (1440,809))
        self.bg218= pygame.transform.scale(self.bg218, (1440,809))
        self.bg219= pygame.transform.scale(self.bg219, (1440,809))
        self.bg220= pygame.transform.scale(self.bg220, (1440,809))
        self.bg221= pygame.transform.scale(self.bg221, (1440,809))
        self.bg222= pygame.transform.scale(self.bg222, (1440,809))
        self.bg223= pygame.transform.scale(self.bg223, (1440,809))
        self.bg224= pygame.transform.scale(self.bg224, (1440,809))
        self.bg225= pygame.transform.scale(self.bg225, (1440,809))
        self.bg226= pygame.transform.scale(self.bg226, (1440,809))
        self.bg227= pygame.transform.scale(self.bg227, (1440,809))
        self.bg228= pygame.transform.scale(self.bg228, (1440,809))
        self.bg229= pygame.transform.scale(self.bg229, (1440,809))
        self.bg230= pygame.transform.scale(self.bg230, (1440,809))
        self.bg231= pygame.transform.scale(self.bg231, (1440,809))
        self.bg232= pygame.transform.scale(self.bg232, (1440,809))
        self.bg233= pygame.transform.scale(self.bg233, (1440,809))
        self.bg234= pygame.transform.scale(self.bg234, (1440,809))
        self.bg235= pygame.transform.scale(self.bg235, (1440,809))
        self.bg236= pygame.transform.scale(self.bg236, (1440,809))
        self.bg237= pygame.transform.scale(self.bg237, (1440,809))
        self.bg238= pygame.transform.scale(self.bg238, (1440,809))
        self.bg239= pygame.transform.scale(self.bg239, (1440,809))
        self.bg240= pygame.transform.scale(self.bg240, (1440,809))
        self.bg241= pygame.transform.scale(self.bg241, (1440,809))
        self.frame = [
            self.bg1,
            self.bg2,
            self.bg3,
            self.bg4,
            self.bg5,
            self.bg6,
            self.bg7,
            self.bg8,
            self.bg9,
            self.bg10,
            self.bg11,
            self.bg12,
            self.bg13,
            self.bg14,
            self.bg15,
            self.bg16,
            self.bg17,
            self.bg18,
            self.bg19,
            self.bg20,
            self.bg21,
            self.bg22,
            self.bg23,
            self.bg24,
            self.bg25,
            self.bg26,
            self.bg27,
            self.bg28,
            self.bg29,
            self.bg30,
            self.bg31,
            self.bg32,
            self.bg33,
            self.bg34,
            self.bg35,
            self.bg36,
            self.bg37,
            self.bg38,
            self.bg39,
            self.bg40,
            self.bg41,
            self.bg42,
            self.bg43,
            self.bg44,
            self.bg45,
            self.bg46,
            self.bg47,
            self.bg48,
            self.bg49,
            self.bg50,
            self.bg51,
            self.bg52,
            self.bg53,
            self.bg54,
            self.bg55,
            self.bg56,
            self.bg57,
            self.bg58,
            self.bg59,
            self.bg60,
            self.bg61,
            self.bg62,
            self.bg63,
            self.bg64,
            self.bg65,
            self.bg66,
            self.bg67,
            self.bg68,
            self.bg69,
            self.bg70,
            self.bg71,
            self.bg72,
            self.bg73,
            self.bg74,
            self.bg75,
            self.bg76,
            self.bg77,
            self.bg78,
            self.bg79,
            self.bg80,
            self.bg81,
            self.bg82,
            self.bg83,
            self.bg84,
            self.bg85,
            self.bg86,
            self.bg87,
            self.bg88,
            self.bg89,
            self.bg90,
            self.bg91,
            self.bg92,
            self.bg93,
            self.bg94,
            self.bg95,
            self.bg96,
            self.bg97,
            self.bg98,
            self.bg99,
            self.bg100,
            self.bg101,
            self.bg102,
            self.bg103,
            self.bg104,
            self.bg105,
            self.bg106,
            self.bg107,
            self.bg108,
            self.bg109,
            self.bg110,
            self.bg111,
            self.bg112,
            self.bg113,
            self.bg114,
            self.bg115,
            self.bg116,
            self.bg117,
            self.bg118,
            self.bg119,
            self.bg120,
            self.bg121,
            self.bg122,
            self.bg123,
            self.bg124,
            self.bg125,
            self.bg126,
            self.bg127,
            self.bg128,
            self.bg129,
            self.bg130,
            self.bg131,
            self.bg132,
            self.bg133,
            self.bg134,
            self.bg135,
            self.bg136,
            self.bg137,
            self.bg138,
            self.bg139,
            self.bg140,
            self.bg141,
            self.bg142,
            self.bg143,
            self.bg144,
            self.bg145,
            self.bg146,
            self.bg147,
            self.bg148,
            self.bg149,
            self.bg150,
            self.bg151,
            self.bg152,
            self.bg153,
            self.bg154,
            self.bg155,
            self.bg156,
            self.bg157,
            self.bg158,
            self.bg159,
            self.bg160,
            self.bg161,
            self.bg162,
            self.bg163,
            self.bg164,
            self.bg165,
            self.bg166,
            self.bg167,
            self.bg168,
            self.bg169,
            self.bg170,
            self.bg171,
            self.bg172,
            self.bg173,
            self.bg174,
            self.bg175,
            self.bg176,
            self.bg177,
            self.bg178,
            self.bg179,
            self.bg180,
            self.bg181,
            self.bg182,
            self.bg183,
            self.bg184,
            self.bg185,
            self.bg186,
            self.bg187,
            self.bg188,
            self.bg189,
            self.bg190,
            self.bg191,
            self.bg192,
            self.bg193,
            self.bg194,
            self.bg195,
            self.bg196,
            self.bg197,
            self.bg198,
            self.bg199,
            self.bg200,
            self.bg201,
            self.bg202,
            self.bg203,
            self.bg204,
            self.bg205,
            self.bg206,
            self.bg207,
            self.bg208,
            self.bg209,
            self.bg210,
            self.bg211,
            self.bg212,
            self.bg213,
            self.bg214,
            self.bg215,
            self.bg216,
            self.bg217,
            self.bg218,
            self.bg219,
            self.bg220,
            self.bg221,
            self.bg222,
            self.bg223,
            self.bg224,
            self.bg225,
            self.bg226,
            self.bg227,
            self.bg228,
            self.bg229,
            self.bg230,
            self.bg231,
            self.bg232,
            self.bg233,
            self.bg234,
            self.bg235,
            self.bg236,
            self.bg237,
            self.bg238,
            self.bg239,
            self.bg240,
            self.bg241,
        ]
        self.FPS = 15
        self.frame_per_second = pygame.time.Clock()


    def play_intro(self):

        self.run_intro = True
        while self.run_intro:
            self.game.display.blit(self.frame[self.number], (0,107.5))
            self.number += 1
            if self.number == 78:
                self.FPS = 10
            if self.number == 241:
                self.game.curr_menu.display_menu()
            self.game.main_menu.update_screen()
            self.frame_per_second.tick(self.FPS)
