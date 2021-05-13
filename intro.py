import pygame

class Intro():
    def __init__(self, game):
        self.game = game
        self.number = 1
        self.timer = 0
        self.bg1 = pygame.image.load("assets/frames_intro/frame (1).jpg")
        self.bg_rect = self.bg1.get_rect()
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
        self.bg242 = pygame.image.load("assets/frames_intro/frame (242).jpg")
        self.bg243 = pygame.image.load("assets/frames_intro/frame (243).jpg")
        self.bg244 = pygame.image.load("assets/frames_intro/frame (244).jpg")
        self.bg245 = pygame.image.load("assets/frames_intro/frame (245).jpg")
        self.bg246 = pygame.image.load("assets/frames_intro/frame (246).jpg")
        self.bg247 = pygame.image.load("assets/frames_intro/frame (247).jpg")
        self.bg248 = pygame.image.load("assets/frames_intro/frame (248).jpg")
        self.bg249 = pygame.image.load("assets/frames_intro/frame (249).jpg")
        self.bg250 = pygame.image.load("assets/frames_intro/frame (250).jpg")
        self.bg251 = pygame.image.load("assets/frames_intro/frame (251).jpg")
        self.bg252 = pygame.image.load("assets/frames_intro/frame (252).jpg")
        self.bg253 = pygame.image.load("assets/frames_intro/frame (253).jpg")
        self.bg254 = pygame.image.load("assets/frames_intro/frame (254).jpg")
        self.bg255 = pygame.image.load("assets/frames_intro/frame (255).jpg")
        self.bg256 = pygame.image.load("assets/frames_intro/frame (256).jpg")
        self.bg257 = pygame.image.load("assets/frames_intro/frame (257).jpg")
        self.bg258 = pygame.image.load("assets/frames_intro/frame (258).jpg")
        self.bg259 = pygame.image.load("assets/frames_intro/frame (259).jpg")
        self.bg260 = pygame.image.load("assets/frames_intro/frame (260).jpg")
        self.bg261 = pygame.image.load("assets/frames_intro/frame (261).jpg")
        self.bg262 = pygame.image.load("assets/frames_intro/frame (262).jpg")
        self.bg263 = pygame.image.load("assets/frames_intro/frame (263).jpg")
        self.bg264 = pygame.image.load("assets/frames_intro/frame (264).jpg")
        self.bg265 = pygame.image.load("assets/frames_intro/frame (265).jpg")
        self.bg266 = pygame.image.load("assets/frames_intro/frame (266).jpg")
        self.bg267 = pygame.image.load("assets/frames_intro/frame (267).jpg")
        self.bg268 = pygame.image.load("assets/frames_intro/frame (268).jpg")
        self.bg269 = pygame.image.load("assets/frames_intro/frame (269).jpg")
        self.bg270 = pygame.image.load("assets/frames_intro/frame (270).jpg")
        self.bg271 = pygame.image.load("assets/frames_intro/frame (271).jpg")
        self.bg272 = pygame.image.load("assets/frames_intro/frame (272).jpg")
        self.bg273 = pygame.image.load("assets/frames_intro/frame (273).jpg")
        self.bg274 = pygame.image.load("assets/frames_intro/frame (274).jpg")
        self.bg275 = pygame.image.load("assets/frames_intro/frame (275).jpg")
        self.bg276 = pygame.image.load("assets/frames_intro/frame (276).jpg")
        self.bg277 = pygame.image.load("assets/frames_intro/frame (277).jpg")
        self.bg278 = pygame.image.load("assets/frames_intro/frame (278).jpg")
        self.bg279 = pygame.image.load("assets/frames_intro/frame (279).jpg")
        self.bg280 = pygame.image.load("assets/frames_intro/frame (280).jpg")
        self.bg281 = pygame.image.load("assets/frames_intro/frame (281).jpg")
        self.bg282 = pygame.image.load("assets/frames_intro/frame (282).jpg")
        self.bg283 = pygame.image.load("assets/frames_intro/frame (283).jpg")
        self.bg284 = pygame.image.load("assets/frames_intro/frame (284).jpg")
        self.bg285 = pygame.image.load("assets/frames_intro/frame (285).jpg")
        self.bg286 = pygame.image.load("assets/frames_intro/frame (286).jpg")
        self.bg287 = pygame.image.load("assets/frames_intro/frame (287).jpg")
        self.bg288 = pygame.image.load("assets/frames_intro/frame (288).jpg")
        self.bg289 = pygame.image.load("assets/frames_intro/frame (289).jpg")
        self.bg290 = pygame.image.load("assets/frames_intro/frame (290).jpg")
        self.bg291 = pygame.image.load("assets/frames_intro/frame (291).jpg")
        self.bg292 = pygame.image.load("assets/frames_intro/frame (292).jpg")
        self.bg293 = pygame.image.load("assets/frames_intro/frame (293).jpg")
        self.bg294 = pygame.image.load("assets/frames_intro/frame (294).jpg")
        self.bg295 = pygame.image.load("assets/frames_intro/frame (295).jpg")
        self.bg296 = pygame.image.load("assets/frames_intro/frame (296).jpg")
        self.bg297 = pygame.image.load("assets/frames_intro/frame (297).jpg")
        self.bg298 = pygame.image.load("assets/frames_intro/frame (298).jpg")
        self.bg299 = pygame.image.load("assets/frames_intro/frame (299).jpg")
        self.bg300 = pygame.image.load("assets/frames_intro/frame (300).jpg")
        self.bg301 = pygame.image.load("assets/frames_intro/frame (301).jpg")
        self.bg302 = pygame.image.load("assets/frames_intro/frame (302).jpg")
        self.bg303 = pygame.image.load("assets/frames_intro/frame (303).jpg")
        self.bg304 = pygame.image.load("assets/frames_intro/frame (304).jpg")
        self.bg305 = pygame.image.load("assets/frames_intro/frame (305).jpg")
        self.bg306 = pygame.image.load("assets/frames_intro/frame (306).jpg")
        self.bg307 = pygame.image.load("assets/frames_intro/frame (307).jpg")
        self.bg308 = pygame.image.load("assets/frames_intro/frame (308).jpg")
        self.bg309 = pygame.image.load("assets/frames_intro/frame (309).jpg")
        self.bg310 = pygame.image.load("assets/frames_intro/frame (310).jpg")
        self.bg311 = pygame.image.load("assets/frames_intro/frame (311).jpg")
        self.bg312 = pygame.image.load("assets/frames_intro/frame (312).jpg")
        self.bg313 = pygame.image.load("assets/frames_intro/frame (313).jpg")
        self.bg314 = pygame.image.load("assets/frames_intro/frame (314).jpg")
        self.bg315 = pygame.image.load("assets/frames_intro/frame (315).jpg")
        self.bg316 = pygame.image.load("assets/frames_intro/frame (316).jpg")
        self.bg317 = pygame.image.load("assets/frames_intro/frame (317).jpg")
        self.bg318 = pygame.image.load("assets/frames_intro/frame (318).jpg")
        self.bg319 = pygame.image.load("assets/frames_intro/frame (319).jpg")
        self.bg320 = pygame.image.load("assets/frames_intro/frame (320).jpg")
        self.bg321 = pygame.image.load("assets/frames_intro/frame (321).jpg")
        self.bg322 = pygame.image.load("assets/frames_intro/frame (322).jpg")
        self.bg323 = pygame.image.load("assets/frames_intro/frame (323).jpg")
        self.bg324 = pygame.image.load("assets/frames_intro/frame (324).jpg")
        self.bg325 = pygame.image.load("assets/frames_intro/frame (325).jpg")
        self.bg326 = pygame.image.load("assets/frames_intro/frame (326).jpg")
        self.bg327 = pygame.image.load("assets/frames_intro/frame (327).jpg")
        self.bg328 = pygame.image.load("assets/frames_intro/frame (328).jpg")
        self.bg329 = pygame.image.load("assets/frames_intro/frame (329).jpg")
        self.bg330 = pygame.image.load("assets/frames_intro/frame (330).jpg")
        self.bg331 = pygame.image.load("assets/frames_intro/frame (331).jpg")
        self.bg332 = pygame.image.load("assets/frames_intro/frame (332).jpg")
        self.bg333 = pygame.image.load("assets/frames_intro/frame (333).jpg")
        self.bg334 = pygame.image.load("assets/frames_intro/frame (334).jpg")
        self.bg335 = pygame.image.load("assets/frames_intro/frame (335).jpg")
        self.bg336 = pygame.image.load("assets/frames_intro/frame (336).jpg")
        self.bg337 = pygame.image.load("assets/frames_intro/frame (337).jpg")
        self.bg338 = pygame.image.load("assets/frames_intro/frame (338).jpg")
        self.bg339 = pygame.image.load("assets/frames_intro/frame (339).jpg")
        self.bg340 = pygame.image.load("assets/frames_intro/frame (340).jpg")
        self.bg341 = pygame.image.load("assets/frames_intro/frame (341).jpg")
        self.bg342 = pygame.image.load("assets/frames_intro/frame (342).jpg")
        self.bg343 = pygame.image.load("assets/frames_intro/frame (343).jpg")
        self.bg344 = pygame.image.load("assets/frames_intro/frame (344).jpg")
        self.bg345 = pygame.image.load("assets/frames_intro/frame (345).jpg")
        self.bg346 = pygame.image.load("assets/frames_intro/frame (346).jpg")
        self.bg347 = pygame.image.load("assets/frames_intro/frame (347).jpg")
        self.bg348 = pygame.image.load("assets/frames_intro/frame (348).jpg")
        self.bg349 = pygame.image.load("assets/frames_intro/frame (349).jpg")
        self.bg350 = pygame.image.load("assets/frames_intro/frame (350).jpg")
        self.bg351 = pygame.image.load("assets/frames_intro/frame (351).jpg")
        self.bg352 = pygame.image.load("assets/frames_intro/frame (352).jpg")
        self.bg353 = pygame.image.load("assets/frames_intro/frame (353).jpg")
        self.bg354 = pygame.image.load("assets/frames_intro/frame (354).jpg")
        self.bg355 = pygame.image.load("assets/frames_intro/frame (355).jpg")
        self.bg356 = pygame.image.load("assets/frames_intro/frame (356).jpg")
        self.bg357 = pygame.image.load("assets/frames_intro/frame (357).jpg")
        self.bg358 = pygame.image.load("assets/frames_intro/frame (358).jpg")
        self.bg359 = pygame.image.load("assets/frames_intro/frame (359).jpg")
        self.bg360 = pygame.image.load("assets/frames_intro/frame (360).jpg")
        self.bg361 = pygame.image.load("assets/frames_intro/frame (361).jpg")
        self.bg362 = pygame.image.load("assets/frames_intro/frame (362).jpg")
        self.bg363 = pygame.image.load("assets/frames_intro/frame (363).jpg")
        self.bg364 = pygame.image.load("assets/frames_intro/frame (364).jpg")
        self.bg365 = pygame.image.load("assets/frames_intro/frame (365).jpg")
        self.bg366 = pygame.image.load("assets/frames_intro/frame (366).jpg")
        self.bg367 = pygame.image.load("assets/frames_intro/frame (367).jpg")
        self.bg368 = pygame.image.load("assets/frames_intro/frame (368).jpg")
        self.bg369 = pygame.image.load("assets/frames_intro/frame (369).jpg")
        self.bg370 = pygame.image.load("assets/frames_intro/frame (370).jpg")
        self.bg371 = pygame.image.load("assets/frames_intro/frame (371).jpg")
        self.bg372 = pygame.image.load("assets/frames_intro/frame (372).jpg")
        self.bg373 = pygame.image.load("assets/frames_intro/frame (373).jpg")
        self.bg374 = pygame.image.load("assets/frames_intro/frame (374).jpg")
        self.bg375 = pygame.image.load("assets/frames_intro/frame (375).jpg")
        self.bg376 = pygame.image.load("assets/frames_intro/frame (376).jpg")
        self.bg377 = pygame.image.load("assets/frames_intro/frame (377).jpg")
        self.bg378 = pygame.image.load("assets/frames_intro/frame (378).jpg")
        self.bg379 = pygame.image.load("assets/frames_intro/frame (379).jpg")
        self.bg380 = pygame.image.load("assets/frames_intro/frame (380).jpg")
        self.bg381 = pygame.image.load("assets/frames_intro/frame (381).jpg")
        self.bg382 = pygame.image.load("assets/frames_intro/frame (382).jpg")
        self.bg383 = pygame.image.load("assets/frames_intro/frame (383).jpg")
        self.bg384 = pygame.image.load("assets/frames_intro/frame (384).jpg")
        self.bg385 = pygame.image.load("assets/frames_intro/frame (385).jpg")
        self.bg386 = pygame.image.load("assets/frames_intro/frame (386).jpg")
        self.bg387 = pygame.image.load("assets/frames_intro/frame (387).jpg")
        self.bg388 = pygame.image.load("assets/frames_intro/frame (388).jpg")
        self.bg389 = pygame.image.load("assets/frames_intro/frame (389).jpg")
        self.bg390 = pygame.image.load("assets/frames_intro/frame (390).jpg")
        self.bg391 = pygame.image.load("assets/frames_intro/frame (391).jpg")
        self.bg392 = pygame.image.load("assets/frames_intro/frame (392).jpg")
        self.bg393 = pygame.image.load("assets/frames_intro/frame (393).jpg")
        self.bg394 = pygame.image.load("assets/frames_intro/frame (394).jpg")
        self.bg395 = pygame.image.load("assets/frames_intro/frame (395).jpg")
        self.bg396 = pygame.image.load("assets/frames_intro/frame (396).jpg")
        self.bg397 = pygame.image.load("assets/frames_intro/frame (397).jpg")
        self.bg398 = pygame.image.load("assets/frames_intro/frame (398).jpg")
        self.bg399 = pygame.image.load("assets/frames_intro/frame (399).jpg")
        self.bg400 = pygame.image.load("assets/frames_intro/frame (400).jpg")
        self.bg401 = pygame.image.load("assets/frames_intro/frame (401).jpg")
        self.bg402 = pygame.image.load("assets/frames_intro/frame (402).jpg")
        self.bg403 = pygame.image.load("assets/frames_intro/frame (403).jpg")
        self.bg404 = pygame.image.load("assets/frames_intro/frame (404).jpg")
        self.bg405 = pygame.image.load("assets/frames_intro/frame (405).jpg")
        self.bg406 = pygame.image.load("assets/frames_intro/frame (406).jpg")
        self.bg407 = pygame.image.load("assets/frames_intro/frame (407).jpg")
        self.bg408 = pygame.image.load("assets/frames_intro/frame (408).jpg")
        self.bg409 = pygame.image.load("assets/frames_intro/frame (409).jpg")
        self.bg410 = pygame.image.load("assets/frames_intro/frame (410).jpg")
        self.bg411 = pygame.image.load("assets/frames_intro/frame (411).jpg")
        self.bg412 = pygame.image.load("assets/frames_intro/frame (412).jpg")
        self.bg413 = pygame.image.load("assets/frames_intro/frame (413).jpg")
        self.bg414 = pygame.image.load("assets/frames_intro/frame (414).jpg")
        self.bg415 = pygame.image.load("assets/frames_intro/frame (415).jpg")
        self.bg416 = pygame.image.load("assets/frames_intro/frame (416).jpg")
        self.bg417 = pygame.image.load("assets/frames_intro/frame (417).jpg")
        self.bg418 = pygame.image.load("assets/frames_intro/frame (418).jpg")
        self.bg419 = pygame.image.load("assets/frames_intro/frame (419).jpg")
        self.bg420 = pygame.image.load("assets/frames_intro/frame (420).jpg")
        self.bg421 = pygame.image.load("assets/frames_intro/frame (421).jpg")
        self.bg422 = pygame.image.load("assets/frames_intro/frame (422).jpg")
        self.bg423 = pygame.image.load("assets/frames_intro/frame (423).jpg")
        self.bg424 = pygame.image.load("assets/frames_intro/frame (424).jpg")
        self.bg425 = pygame.image.load("assets/frames_intro/frame (425).jpg")
        self.bg426 = pygame.image.load("assets/frames_intro/frame (426).jpg")
        self.bg427 = pygame.image.load("assets/frames_intro/frame (427).jpg")
        self.bg428 = pygame.image.load("assets/frames_intro/frame (428).jpg")
        self.bg429 = pygame.image.load("assets/frames_intro/frame (429).jpg")
        self.bg430 = pygame.image.load("assets/frames_intro/frame (430).jpg")
        self.bg431 = pygame.image.load("assets/frames_intro/frame (431).jpg")
        self.bg432 = pygame.image.load("assets/frames_intro/frame (432).jpg")
        self.bg433 = pygame.image.load("assets/frames_intro/frame (433).jpg")
        self.bg434 = pygame.image.load("assets/frames_intro/frame (434).jpg")
        self.bg435 = pygame.image.load("assets/frames_intro/frame (435).jpg")
        self.bg436 = pygame.image.load("assets/frames_intro/frame (436).jpg")
        self.bg437 = pygame.image.load("assets/frames_intro/frame (437).jpg")
        self.bg438 = pygame.image.load("assets/frames_intro/frame (438).jpg")
        self.bg439 = pygame.image.load("assets/frames_intro/frame (439).jpg")
        self.bg440 = pygame.image.load("assets/frames_intro/frame (440).jpg")
        self.bg441 = pygame.image.load("assets/frames_intro/frame (441).jpg")
        self.bg442 = pygame.image.load("assets/frames_intro/frame (442).jpg")
        self.bg443 = pygame.image.load("assets/frames_intro/frame (443).jpg")
        self.bg444 = pygame.image.load("assets/frames_intro/frame (444).jpg")
        self.bg445 = pygame.image.load("assets/frames_intro/frame (445).jpg")
        self.bg446 = pygame.image.load("assets/frames_intro/frame (446).jpg")
        self.bg447 = pygame.image.load("assets/frames_intro/frame (447).jpg")
        self.bg448 = pygame.image.load("assets/frames_intro/frame (448).jpg")
        self.bg449 = pygame.image.load("assets/frames_intro/frame (449).jpg")
        self.bg450 = pygame.image.load("assets/frames_intro/frame (450).jpg")
        self.bg451 = pygame.image.load("assets/frames_intro/frame (451).jpg")
        self.bg452 = pygame.image.load("assets/frames_intro/frame (452).jpg")
        self.bg453 = pygame.image.load("assets/frames_intro/frame (453).jpg")
        self.bg454 = pygame.image.load("assets/frames_intro/frame (454).jpg")
        self.bg455 = pygame.image.load("assets/frames_intro/frame (455).jpg")
        self.bg456 = pygame.image.load("assets/frames_intro/frame (456).jpg")
        self.bg457 = pygame.image.load("assets/frames_intro/frame (457).jpg")
        self.bg458 = pygame.image.load("assets/frames_intro/frame (458).jpg")
        self.bg459 = pygame.image.load("assets/frames_intro/frame (459).jpg")
        self.bg460 = pygame.image.load("assets/frames_intro/frame (460).jpg")
        self.bg461 = pygame.image.load("assets/frames_intro/frame (461).jpg")
        self.bg462 = pygame.image.load("assets/frames_intro/frame (462).jpg")
        self.bg463 = pygame.image.load("assets/frames_intro/frame (463).jpg")
        self.bg464 = pygame.image.load("assets/frames_intro/frame (464).jpg")
        self.bg465 = pygame.image.load("assets/frames_intro/frame (465).jpg")
        self.bg466 = pygame.image.load("assets/frames_intro/frame (466).jpg")
        self.bg467 = pygame.image.load("assets/frames_intro/frame (467).jpg")
        self.bg468 = pygame.image.load("assets/frames_intro/frame (468).jpg")
        self.bg469 = pygame.image.load("assets/frames_intro/frame (469).jpg")
        self.bg470 = pygame.image.load("assets/frames_intro/frame (470).jpg")
        self.bg471 = pygame.image.load("assets/frames_intro/frame (471).jpg")
        self.bg472 = pygame.image.load("assets/frames_intro/frame (472).jpg")
        self.bg473 = pygame.image.load("assets/frames_intro/frame (473).jpg")
        self.bg474 = pygame.image.load("assets/frames_intro/frame (474).jpg")
        self.bg475 = pygame.image.load("assets/frames_intro/frame (475).jpg")
        self.bg476 = pygame.image.load("assets/frames_intro/frame (476).jpg")
        self.bg477 = pygame.image.load("assets/frames_intro/frame (477).jpg")
        self.bg478 = pygame.image.load("assets/frames_intro/frame (478).jpg")
        self.bg479 = pygame.image.load("assets/frames_intro/frame (479).jpg")
        self.bg480 = pygame.image.load("assets/frames_intro/frame (480).jpg")
        self.bg481 = pygame.image.load("assets/frames_intro/frame (481).jpg")
        self.bg482 = pygame.image.load("assets/frames_intro/frame (482).jpg")
        self.bg483 = pygame.image.load("assets/frames_intro/frame (483).jpg")
        self.bg484 = pygame.image.load("assets/frames_intro/frame (484).jpg")
        self.bg485 = pygame.image.load("assets/frames_intro/frame (485).jpg")
        self.bg486 = pygame.image.load("assets/frames_intro/frame (486).jpg")
        self.bg487 = pygame.image.load("assets/frames_intro/frame (487).jpg")
        self.bg488 = pygame.image.load("assets/frames_intro/frame (488).jpg")
        self.bg489 = pygame.image.load("assets/frames_intro/frame (489).jpg")
        self.bg490 = pygame.image.load("assets/frames_intro/frame (490).jpg")
        self.bg491 = pygame.image.load("assets/frames_intro/frame (491).jpg")
        self.bg492 = pygame.image.load("assets/frames_intro/frame (492).jpg")
        self.bg493 = pygame.image.load("assets/frames_intro/frame (493).jpg")
        self.bg494 = pygame.image.load("assets/frames_intro/frame (494).jpg")
        self.bg495 = pygame.image.load("assets/frames_intro/frame (495).jpg")
        self.bg496 = pygame.image.load("assets/frames_intro/frame (496).jpg")
        self.bg497 = pygame.image.load("assets/frames_intro/frame (497).jpg")
        self.bg498 = pygame.image.load("assets/frames_intro/frame (498).jpg")
        self.bg499 = pygame.image.load("assets/frames_intro/frame (499).jpg")
        self.bg500 = pygame.image.load("assets/frames_intro/frame (500).jpg")
        self.bg501 = pygame.image.load("assets/frames_intro/frame (501).jpg")
        self.bg502 = pygame.image.load("assets/frames_intro/frame (502).jpg")
        self.bg503 = pygame.image.load("assets/frames_intro/frame (503).jpg")
        self.bg504 = pygame.image.load("assets/frames_intro/frame (504).jpg")
        self.bg505 = pygame.image.load("assets/frames_intro/frame (505).jpg")
        self.bg506 = pygame.image.load("assets/frames_intro/frame (506).jpg")
        self.bg507 = pygame.image.load("assets/frames_intro/frame (507).jpg")
        self.bg508 = pygame.image.load("assets/frames_intro/frame (508).jpg")
        self.bg509 = pygame.image.load("assets/frames_intro/frame (509).jpg")
        self.bg510 = pygame.image.load("assets/frames_intro/frame (510).jpg")
        self.bg511 = pygame.image.load("assets/frames_intro/frame (511).jpg")
        self.bg512 = pygame.image.load("assets/frames_intro/frame (512).jpg")
        self.bg513 = pygame.image.load("assets/frames_intro/frame (513).jpg")
        self.bg514 = pygame.image.load("assets/frames_intro/frame (514).jpg")
        self.bg515 = pygame.image.load("assets/frames_intro/frame (515).jpg")
        self.bg516 = pygame.image.load("assets/frames_intro/frame (516).jpg")
        self.bg517 = pygame.image.load("assets/frames_intro/frame (517).jpg")
        self.bg518 = pygame.image.load("assets/frames_intro/frame (518).jpg")
        self.bg519 = pygame.image.load("assets/frames_intro/frame (519).jpg")
        self.bg520 = pygame.image.load("assets/frames_intro/frame (520).jpg")
        self.bg521 = pygame.image.load("assets/frames_intro/frame (521).jpg")
        self.bg522 = pygame.image.load("assets/frames_intro/frame (522).jpg")
        self.bg523 = pygame.image.load("assets/frames_intro/frame (523).jpg")
        self.bg524 = pygame.image.load("assets/frames_intro/frame (524).jpg")
        self.bg525 = pygame.image.load("assets/frames_intro/frame (525).jpg")
        self.bg526 = pygame.image.load("assets/frames_intro/frame (526).jpg")
        self.bg527 = pygame.image.load("assets/frames_intro/frame (527).jpg")
        self.bg528 = pygame.image.load("assets/frames_intro/frame (528).jpg")
        self.bg529 = pygame.image.load("assets/frames_intro/frame (529).jpg")
        self.bg530 = pygame.image.load("assets/frames_intro/frame (530).jpg")
        self.bg531 = pygame.image.load("assets/frames_intro/frame (531).jpg")
        self.bg532 = pygame.image.load("assets/frames_intro/frame (532).jpg")
        self.bg533 = pygame.image.load("assets/frames_intro/frame (533).jpg")
        self.bg534 = pygame.image.load("assets/frames_intro/frame (534).jpg")
        self.bg535 = pygame.image.load("assets/frames_intro/frame (535).jpg")
        self.bg536 = pygame.image.load("assets/frames_intro/frame (536).jpg")
        self.bg537 = pygame.image.load("assets/frames_intro/frame (537).jpg")
        self.bg538 = pygame.image.load("assets/frames_intro/frame (538).jpg")
        self.bg539 = pygame.image.load("assets/frames_intro/frame (539).jpg")
        self.bg540 = pygame.image.load("assets/frames_intro/frame (540).jpg")
        self.bg541 = pygame.image.load("assets/frames_intro/frame (541).jpg")
        self.bg542 = pygame.image.load("assets/frames_intro/frame (542).jpg")
        self.bg543 = pygame.image.load("assets/frames_intro/frame (543).jpg")
        self.bg544 = pygame.image.load("assets/frames_intro/frame (544).jpg")
        self.bg545 = pygame.image.load("assets/frames_intro/frame (545).jpg")
        self.bg546 = pygame.image.load("assets/frames_intro/frame (546).jpg")
        self.bg547 = pygame.image.load("assets/frames_intro/frame (547).jpg")
        self.bg548 = pygame.image.load("assets/frames_intro/frame (548).jpg")
        self.bg549 = pygame.image.load("assets/frames_intro/frame (549).jpg")
        self.bg550 = pygame.image.load("assets/frames_intro/frame (550).jpg")
        self.bg551 = pygame.image.load("assets/frames_intro/frame (551).jpg")
        self.bg552 = pygame.image.load("assets/frames_intro/frame (552).jpg")
        self.bg553 = pygame.image.load("assets/frames_intro/frame (553).jpg")
        self.bg554 = pygame.image.load("assets/frames_intro/frame (554).jpg")
        self.bg555 = pygame.image.load("assets/frames_intro/frame (555).jpg")
        self.bg556 = pygame.image.load("assets/frames_intro/frame (556).jpg")
        self.bg557 = pygame.image.load("assets/frames_intro/frame (557).jpg")
        self.bg558 = pygame.image.load("assets/frames_intro/frame (558).jpg")
        self.bg559 = pygame.image.load("assets/frames_intro/frame (559).jpg")
        self.bg560 = pygame.image.load("assets/frames_intro/frame (560).jpg")
        self.bg561 = pygame.image.load("assets/frames_intro/frame (561).jpg")
        self.bg562 = pygame.image.load("assets/frames_intro/frame (562).jpg")
        self.bg563 = pygame.image.load("assets/frames_intro/frame (563).jpg")
        self.bg564 = pygame.image.load("assets/frames_intro/frame (564).jpg")
        self.bg565 = pygame.image.load("assets/frames_intro/frame (565).jpg")
        self.bg566 = pygame.image.load("assets/frames_intro/frame (566).jpg")
        self.bg567 = pygame.image.load("assets/frames_intro/frame (567).jpg")
        self.bg568 = pygame.image.load("assets/frames_intro/frame (568).jpg")
        self.bg569 = pygame.image.load("assets/frames_intro/frame (569).jpg")
        self.bg570 = pygame.image.load("assets/frames_intro/frame (570).jpg")
        self.bg571 = pygame.image.load("assets/frames_intro/frame (571).jpg")
        self.bg572 = pygame.image.load("assets/frames_intro/frame (572).jpg")
        self.bg573 = pygame.image.load("assets/frames_intro/frame (573).jpg")
        self.bg574 = pygame.image.load("assets/frames_intro/frame (574).jpg")
        self.bg575 = pygame.image.load("assets/frames_intro/frame (575).jpg")
        self.bg576 = pygame.image.load("assets/frames_intro/frame (576).jpg")
        self.bg577 = pygame.image.load("assets/frames_intro/frame (577).jpg")
        self.bg578 = pygame.image.load("assets/frames_intro/frame (578).jpg")
        self.bg579 = pygame.image.load("assets/frames_intro/frame (579).jpg")
        self.bg580 = pygame.image.load("assets/frames_intro/frame (580).jpg")
        self.bg581 = pygame.image.load("assets/frames_intro/frame (581).jpg")
        self.bg582 = pygame.image.load("assets/frames_intro/frame (582).jpg")
        self.bg583 = pygame.image.load("assets/frames_intro/frame (583).jpg")
        # self.bg1 = pygame.transform.scale(self.bg1, (1440,809))
        # self.bg2 = pygame.transform.scale(self.bg2, (1440,809))
        # self.bg3 = pygame.transform.scale(self.bg3, (1440,809))
        # self.bg4 = pygame.transform.scale(self.bg4, (1440,809))
        # self.bg5 = pygame.transform.scale(self.bg5, (1440,809))
        # self.bg6 = pygame.transform.scale(self.bg6, (1440,809))
        # self.bg7 = pygame.transform.scale(self.bg7, (1440,809))
        # self.bg8 = pygame.transform.scale(self.bg8, (1440,809))
        # self.bg9 = pygame.transform.scale(self.bg9, (1440,809))
        # self.bg10 = pygame.transform.scale(self.bg10, (1440,809))
        # self.bg11 = pygame.transform.scale(self.bg11, (1440,809))
        # self.bg12 = pygame.transform.scale(self.bg12, (1440,809))
        # self.bg13 = pygame.transform.scale(self.bg13, (1440,809))
        # self.bg14 = pygame.transform.scale(self.bg14, (1440,809))
        # self.bg15 = pygame.transform.scale(self.bg15, (1440,809))
        # self.bg16 = pygame.transform.scale(self.bg16, (1440,809))
        # self.bg17 = pygame.transform.scale(self.bg17, (1440,809))
        # self.bg18 = pygame.transform.scale(self.bg18, (1440,809))
        # self.bg19 = pygame.transform.scale(self.bg19, (1440,809))
        # self.bg20 = pygame.transform.scale(self.bg20, (1440,809))
        # self.bg21 = pygame.transform.scale(self.bg21, (1440,809))
        # self.bg22 = pygame.transform.scale(self.bg22, (1440,809))
        # self.bg23 = pygame.transform.scale(self.bg23, (1440,809))
        # self.bg24 = pygame.transform.scale(self.bg24, (1440,809))
        # self.bg25 = pygame.transform.scale(self.bg25, (1440,809))
        # self.bg26 = pygame.transform.scale(self.bg26, (1440,809))
        # self.bg27 = pygame.transform.scale(self.bg27, (1440,809))
        # self.bg28 = pygame.transform.scale(self.bg28, (1440,809))
        # self.bg29 = pygame.transform.scale(self.bg29, (1440,809))
        # self.bg30 = pygame.transform.scale(self.bg30, (1440,809))
        # self.bg31 = pygame.transform.scale(self.bg31, (1440,809))
        # self.bg32 = pygame.transform.scale(self.bg32, (1440,809))
        # self.bg33 = pygame.transform.scale(self.bg33, (1440,809))
        # self.bg34 = pygame.transform.scale(self.bg34, (1440,809))
        # self.bg35 = pygame.transform.scale(self.bg35, (1440,809))
        # self.bg36 = pygame.transform.scale(self.bg36, (1440,809))
        # self.bg37 = pygame.transform.scale(self.bg37, (1440,809))
        # self.bg38 = pygame.transform.scale(self.bg38, (1440,809))
        # self.bg39 = pygame.transform.scale(self.bg39, (1440,809))
        # self.bg40 = pygame.transform.scale(self.bg40, (1440,809))
        # self.bg41 = pygame.transform.scale(self.bg41, (1440,809))
        # self.bg42 = pygame.transform.scale(self.bg42, (1440,809))
        # self.bg43 = pygame.transform.scale(self.bg43, (1440,809))
        # self.bg44 = pygame.transform.scale(self.bg44, (1440,809))
        # self.bg45 = pygame.transform.scale(self.bg45, (1440,809))
        # self.bg46 = pygame.transform.scale(self.bg46, (1440,809))
        # self.bg47 = pygame.transform.scale(self.bg47, (1440,809))
        # self.bg48 = pygame.transform.scale(self.bg48, (1440,809))
        # self.bg49 = pygame.transform.scale(self.bg49, (1440,809))
        # self.bg50 = pygame.transform.scale(self.bg50, (1440,809))
        # self.bg51 = pygame.transform.scale(self.bg51, (1440,809))
        # self.bg52 = pygame.transform.scale(self.bg52, (1440,809))
        # self.bg53 = pygame.transform.scale(self.bg53, (1440,809))
        # self.bg54 = pygame.transform.scale(self.bg54, (1440,809))
        # self.bg55 = pygame.transform.scale(self.bg55, (1440,809))
        # self.bg56 = pygame.transform.scale(self.bg56, (1440,809))
        # self.bg57 = pygame.transform.scale(self.bg57, (1440,809))
        # self.bg58 = pygame.transform.scale(self.bg58, (1440,809))
        # self.bg59 = pygame.transform.scale(self.bg59, (1440,809))
        # self.bg60 = pygame.transform.scale(self.bg60, (1440,809))
        # self.bg61 = pygame.transform.scale(self.bg61, (1440,809))
        # self.bg62 = pygame.transform.scale(self.bg62, (1440,809))
        # self.bg63 = pygame.transform.scale(self.bg63, (1440,809))
        # self.bg64 = pygame.transform.scale(self.bg64, (1440,809))
        # self.bg65 = pygame.transform.scale(self.bg65, (1440,809))
        # self.bg66 = pygame.transform.scale(self.bg66, (1440,809))
        # self.bg67 = pygame.transform.scale(self.bg67, (1440,809))
        # self.bg68 = pygame.transform.scale(self.bg68, (1440,809))
        # self.bg69 = pygame.transform.scale(self.bg69, (1440,809))
        # self.bg70 = pygame.transform.scale(self.bg70, (1440,809))
        # self.bg71 = pygame.transform.scale(self.bg71, (1440,809))
        # self.bg72 = pygame.transform.scale(self.bg72, (1440,809))
        # self.bg73 = pygame.transform.scale(self.bg73, (1440,809))
        # self.bg74 = pygame.transform.scale(self.bg74, (1440,809))
        # self.bg75 = pygame.transform.scale(self.bg75, (1440,809))
        # self.bg76 = pygame.transform.scale(self.bg76, (1440,809))
        # self.bg77 = pygame.transform.scale(self.bg77, (1440,809))
        # self.bg78 = pygame.transform.scale(self.bg78, (1440,809))
        # self.bg79 = pygame.transform.scale(self.bg79, (1440,809))
        # self.bg80 = pygame.transform.scale(self.bg80, (1440,809))
        # self.bg81 = pygame.transform.scale(self.bg81, (1440,809))
        # self.bg82 = pygame.transform.scale(self.bg82, (1440,809))
        # self.bg83 = pygame.transform.scale(self.bg83, (1440,809))
        # self.bg84 = pygame.transform.scale(self.bg84, (1440,809))
        # self.bg85 = pygame.transform.scale(self.bg85, (1440,809))
        # self.bg86 = pygame.transform.scale(self.bg86, (1440,809))
        # self.bg87 = pygame.transform.scale(self.bg87, (1440,809))
        # self.bg88 = pygame.transform.scale(self.bg88, (1440,809))
        # self.bg89 = pygame.transform.scale(self.bg89, (1440,809))
        # self.bg90 = pygame.transform.scale(self.bg90, (1440,809))
        # self.bg91 = pygame.transform.scale(self.bg91, (1440,809))
        # self.bg92 = pygame.transform.scale(self.bg92, (1440,809))
        # self.bg93 = pygame.transform.scale(self.bg93, (1440,809))
        # self.bg94 = pygame.transform.scale(self.bg94, (1440,809))
        # self.bg95 = pygame.transform.scale(self.bg95, (1440,809))
        # self.bg96 = pygame.transform.scale(self.bg96, (1440,809))
        # self.bg97 = pygame.transform.scale(self.bg97, (1440,809))
        # self.bg98 = pygame.transform.scale(self.bg98, (1440,809))
        # self.bg99 = pygame.transform.scale(self.bg99, (1440,809))
        # self.bg100 = pygame.transform.scale(self.bg100, (1440,809))
        # self.bg101 = pygame.transform.scale(self.bg101, (1440,809))
        # self.bg102 = pygame.transform.scale(self.bg102, (1440,809))
        # self.bg103 = pygame.transform.scale(self.bg103, (1440,809))
        # self.bg104 = pygame.transform.scale(self.bg104, (1440,809))
        # self.bg105 = pygame.transform.scale(self.bg105, (1440,809))
        # self.bg106 = pygame.transform.scale(self.bg106, (1440,809))
        # self.bg107 = pygame.transform.scale(self.bg107, (1440,809))
        # self.bg108 = pygame.transform.scale(self.bg108, (1440,809))
        # self.bg109 = pygame.transform.scale(self.bg109, (1440,809))
        # self.bg110 = pygame.transform.scale(self.bg110, (1440,809))
        # self.bg111 = pygame.transform.scale(self.bg111, (1440,809))
        # self.bg112 = pygame.transform.scale(self.bg112, (1440,809))
        # self.bg113 = pygame.transform.scale(self.bg113, (1440,809))
        # self.bg114 = pygame.transform.scale(self.bg114, (1440,809))
        # self.bg115 = pygame.transform.scale(self.bg115, (1440,809))
        # self.bg116 = pygame.transform.scale(self.bg116, (1440,809))
        # self.bg117 = pygame.transform.scale(self.bg117, (1440,809))
        # self.bg118 = pygame.transform.scale(self.bg118, (1440,809))
        # self.bg119 = pygame.transform.scale(self.bg119, (1440,809))
        # self.bg120 = pygame.transform.scale(self.bg120, (1440,809))
        # self.bg121 = pygame.transform.scale(self.bg121, (1440,809))
        # self.bg122 = pygame.transform.scale(self.bg122, (1440,809))
        # self.bg123 = pygame.transform.scale(self.bg123, (1440,809))
        # self.bg124 = pygame.transform.scale(self.bg124, (1440,809))
        # self.bg125 = pygame.transform.scale(self.bg125, (1440,809))
        # self.bg126 = pygame.transform.scale(self.bg126, (1440,809))
        # self.bg127 = pygame.transform.scale(self.bg127, (1440,809))
        # self.bg128 = pygame.transform.scale(self.bg128, (1440,809))
        # self.bg129 = pygame.transform.scale(self.bg129, (1440,809))
        # self.bg130 = pygame.transform.scale(self.bg130, (1440,809))
        # self.bg131 = pygame.transform.scale(self.bg131, (1440,809))
        # self.bg132 = pygame.transform.scale(self.bg132, (1440,809))
        # self.bg133 = pygame.transform.scale(self.bg133, (1440,809))
        # self.bg134 = pygame.transform.scale(self.bg134, (1440,809))
        # self.bg135 = pygame.transform.scale(self.bg135, (1440,809))
        # self.bg136 = pygame.transform.scale(self.bg136, (1440,809))
        # self.bg137 = pygame.transform.scale(self.bg137, (1440,809))
        # self.bg138 = pygame.transform.scale(self.bg138, (1440,809))
        # self.bg139 = pygame.transform.scale(self.bg139, (1440,809))
        # self.bg140 = pygame.transform.scale(self.bg140, (1440,809))
        # self.bg141 = pygame.transform.scale(self.bg141, (1440,809))
        # self.bg142 = pygame.transform.scale(self.bg142, (1440,809))
        # self.bg143 = pygame.transform.scale(self.bg143, (1440,809))
        # self.bg144 = pygame.transform.scale(self.bg144, (1440,809))
        # self.bg145 = pygame.transform.scale(self.bg145, (1440,809))
        # self.bg146 = pygame.transform.scale(self.bg146, (1440,809))
        # self.bg147 = pygame.transform.scale(self.bg147, (1440,809))
        # self.bg148 = pygame.transform.scale(self.bg148, (1440,809))
        # self.bg149 = pygame.transform.scale(self.bg149, (1440,809))
        # self.bg150 = pygame.transform.scale(self.bg150, (1440,809))
        # self.bg151 = pygame.transform.scale(self.bg151, (1440,809))
        # self.bg152 = pygame.transform.scale(self.bg152, (1440,809))
        # self.bg153 = pygame.transform.scale(self.bg153, (1440,809))
        # self.bg154 = pygame.transform.scale(self.bg154, (1440,809))
        # self.bg155 = pygame.transform.scale(self.bg155, (1440,809))
        # self.bg156 = pygame.transform.scale(self.bg156, (1440,809))
        # self.bg157 = pygame.transform.scale(self.bg157, (1440,809))
        # self.bg158 = pygame.transform.scale(self.bg158, (1440,809))
        # self.bg159 = pygame.transform.scale(self.bg159, (1440,809))
        # self.bg160 = pygame.transform.scale(self.bg160, (1440,809))
        # self.bg161 = pygame.transform.scale(self.bg161, (1440,809))
        # self.bg162 = pygame.transform.scale(self.bg162, (1440,809))
        # self.bg163 = pygame.transform.scale(self.bg163, (1440,809))
        # self.bg164 = pygame.transform.scale(self.bg164, (1440,809))
        # self.bg165 = pygame.transform.scale(self.bg165, (1440,809))
        # self.bg166 = pygame.transform.scale(self.bg166, (1440,809))
        # self.bg167 = pygame.transform.scale(self.bg167, (1440,809))
        # self.bg168 = pygame.transform.scale(self.bg168, (1440,809))
        # self.bg169 = pygame.transform.scale(self.bg169, (1440,809))
        # self.bg170 = pygame.transform.scale(self.bg170, (1440,809))
        # self.bg171 = pygame.transform.scale(self.bg171, (1440,809))
        # self.bg172 = pygame.transform.scale(self.bg172, (1440,809))
        # self.bg173 = pygame.transform.scale(self.bg173, (1440,809))
        # self.bg174 = pygame.transform.scale(self.bg174, (1440,809))
        # self.bg175 = pygame.transform.scale(self.bg175, (1440,809))
        # self.bg176 = pygame.transform.scale(self.bg176, (1440,809))
        # self.bg177 = pygame.transform.scale(self.bg177, (1440,809))
        # self.bg178 = pygame.transform.scale(self.bg178, (1440,809))
        # self.bg179 = pygame.transform.scale(self.bg179, (1440,809))
        # self.bg180 = pygame.transform.scale(self.bg180, (1440,809))
        # self.bg181 = pygame.transform.scale(self.bg181, (1440,809))
        # self.bg182 = pygame.transform.scale(self.bg182, (1440,809))
        # self.bg183 = pygame.transform.scale(self.bg183, (1440,809))
        # self.bg184 = pygame.transform.scale(self.bg184, (1440,809))
        # self.bg185 = pygame.transform.scale(self.bg185, (1440,809))
        # self.bg186 = pygame.transform.scale(self.bg186, (1440,809))
        # self.bg187 = pygame.transform.scale(self.bg187, (1440,809))
        # self.bg188 = pygame.transform.scale(self.bg188, (1440,809))
        # self.bg189 = pygame.transform.scale(self.bg189, (1440,809))
        # self.bg190 = pygame.transform.scale(self.bg190, (1440,809))
        # self.bg191 = pygame.transform.scale(self.bg191, (1440,809))
        # self.bg192 = pygame.transform.scale(self.bg192, (1440,809))
        # self.bg193 = pygame.transform.scale(self.bg193, (1440,809))
        # self.bg194 = pygame.transform.scale(self.bg194, (1440,809))
        # self.bg195 = pygame.transform.scale(self.bg195, (1440,809))
        # self.bg196 = pygame.transform.scale(self.bg196, (1440,809))
        # self.bg197 = pygame.transform.scale(self.bg197, (1440,809))
        # self.bg198 = pygame.transform.scale(self.bg198, (1440,809))
        # self.bg199 = pygame.transform.scale(self.bg199, (1440,809))
        # self.bg200 = pygame.transform.scale(self.bg200, (1440,809))
        # self.bg201 = pygame.transform.scale(self.bg201, (1440,809))
        # self.bg202 = pygame.transform.scale(self.bg202, (1440,809))
        # self.bg203 = pygame.transform.scale(self.bg203, (1440,809))
        # self.bg204 = pygame.transform.scale(self.bg204, (1440,809))
        # self.bg205 = pygame.transform.scale(self.bg205, (1440,809))
        # self.bg206 = pygame.transform.scale(self.bg206, (1440,809))
        # self.bg207 = pygame.transform.scale(self.bg207, (1440,809))
        # self.bg208 = pygame.transform.scale(self.bg208, (1440,809))
        # self.bg209 = pygame.transform.scale(self.bg209, (1440,809))
        # self.bg210 = pygame.transform.scale(self.bg210, (1440,809))
        # self.bg211 = pygame.transform.scale(self.bg211, (1440,809))
        # self.bg212 = pygame.transform.scale(self.bg212, (1440,809))
        # self.bg213 = pygame.transform.scale(self.bg213, (1440,809))
        # self.bg214 = pygame.transform.scale(self.bg214, (1440,809))
        # self.bg215 = pygame.transform.scale(self.bg215, (1440,809))
        # self.bg216 = pygame.transform.scale(self.bg216, (1440,809))
        # self.bg217 = pygame.transform.scale(self.bg217, (1440,809))
        # self.bg218 = pygame.transform.scale(self.bg218, (1440,809))
        # self.bg219 = pygame.transform.scale(self.bg219, (1440,809))
        # self.bg220 = pygame.transform.scale(self.bg220, (1440,809))
        # self.bg221 = pygame.transform.scale(self.bg221, (1440,809))
        # self.bg222 = pygame.transform.scale(self.bg222, (1440,809))
        # self.bg223 = pygame.transform.scale(self.bg223, (1440,809))
        # self.bg224 = pygame.transform.scale(self.bg224, (1440,809))
        # self.bg225 = pygame.transform.scale(self.bg225, (1440,809))
        # self.bg226 = pygame.transform.scale(self.bg226, (1440,809))
        # self.bg227 = pygame.transform.scale(self.bg227, (1440,809))
        # self.bg228 = pygame.transform.scale(self.bg228, (1440,809))
        # self.bg229 = pygame.transform.scale(self.bg229, (1440,809))
        # self.bg230 = pygame.transform.scale(self.bg230, (1440,809))
        # self.bg231 = pygame.transform.scale(self.bg231, (1440,809))
        # self.bg232 = pygame.transform.scale(self.bg232, (1440,809))
        # self.bg233 = pygame.transform.scale(self.bg233, (1440,809))
        # self.bg234 = pygame.transform.scale(self.bg234, (1440,809))
        # self.bg235 = pygame.transform.scale(self.bg235, (1440,809))
        # self.bg236 = pygame.transform.scale(self.bg236, (1440,809))
        # self.bg237 = pygame.transform.scale(self.bg237, (1440,809))
        # self.bg238 = pygame.transform.scale(self.bg238, (1440,809))
        # self.bg239 = pygame.transform.scale(self.bg239, (1440,809))
        # self.bg240 = pygame.transform.scale(self.bg240, (1440,809))
        # self.bg241 = pygame.transform.scale(self.bg241, (1440,809))
        # self.bg242 = pygame.transform.scale(self.bg242, (1440,809))
        # self.bg243 = pygame.transform.scale(self.bg243, (1440,809))
        # self.bg244 = pygame.transform.scale(self.bg244, (1440,809))
        # self.bg245 = pygame.transform.scale(self.bg245, (1440,809))
        # self.bg246 = pygame.transform.scale(self.bg246, (1440,809))
        # self.bg247 = pygame.transform.scale(self.bg247, (1440,809))
        # self.bg248 = pygame.transform.scale(self.bg248, (1440,809))
        # self.bg249 = pygame.transform.scale(self.bg249, (1440,809))
        # self.bg250 = pygame.transform.scale(self.bg250, (1440,809))
        # self.bg251 = pygame.transform.scale(self.bg251, (1440,809))
        # self.bg252 = pygame.transform.scale(self.bg252, (1440,809))
        # self.bg253 = pygame.transform.scale(self.bg253, (1440,809))
        # self.bg254 = pygame.transform.scale(self.bg254, (1440,809))
        # self.bg255 = pygame.transform.scale(self.bg255, (1440,809))
        # self.bg256 = pygame.transform.scale(self.bg256, (1440,809))
        # self.bg257 = pygame.transform.scale(self.bg257, (1440,809))
        # self.bg258 = pygame.transform.scale(self.bg258, (1440,809))
        # self.bg259 = pygame.transform.scale(self.bg259, (1440,809))
        # self.bg260 = pygame.transform.scale(self.bg260, (1440,809))
        # self.bg261 = pygame.transform.scale(self.bg261, (1440,809))
        # self.bg262 = pygame.transform.scale(self.bg262, (1440,809))
        # self.bg263 = pygame.transform.scale(self.bg263, (1440,809))
        # self.bg264 = pygame.transform.scale(self.bg264, (1440,809))
        # self.bg265 = pygame.transform.scale(self.bg265, (1440,809))
        # self.bg266 = pygame.transform.scale(self.bg266, (1440,809))
        # self.bg267 = pygame.transform.scale(self.bg267, (1440,809))
        # self.bg268 = pygame.transform.scale(self.bg268, (1440,809))
        # self.bg269 = pygame.transform.scale(self.bg269, (1440,809))
        # self.bg270 = pygame.transform.scale(self.bg270, (1440,809))
        # self.bg271 = pygame.transform.scale(self.bg271, (1440,809))
        # self.bg272 = pygame.transform.scale(self.bg272, (1440,809))
        # self.bg273 = pygame.transform.scale(self.bg273, (1440,809))
        # self.bg274 = pygame.transform.scale(self.bg274, (1440,809))
        # self.bg275 = pygame.transform.scale(self.bg275, (1440,809))
        # self.bg276 = pygame.transform.scale(self.bg276, (1440,809))
        # self.bg277 = pygame.transform.scale(self.bg277, (1440,809))
        # self.bg278 = pygame.transform.scale(self.bg278, (1440,809))
        # self.bg279 = pygame.transform.scale(self.bg279, (1440,809))
        # self.bg280 = pygame.transform.scale(self.bg280, (1440,809))
        # self.bg281 = pygame.transform.scale(self.bg281, (1440,809))
        # self.bg282 = pygame.transform.scale(self.bg282, (1440,809))
        # self.bg283 = pygame.transform.scale(self.bg283, (1440,809))
        # self.bg284 = pygame.transform.scale(self.bg284, (1440,809))
        # self.bg285 = pygame.transform.scale(self.bg285, (1440,809))
        # self.bg286 = pygame.transform.scale(self.bg286, (1440,809))
        # self.bg287 = pygame.transform.scale(self.bg287, (1440,809))
        # self.bg288 = pygame.transform.scale(self.bg288, (1440,809))
        # self.bg289 = pygame.transform.scale(self.bg289, (1440,809))
        # self.bg290 = pygame.transform.scale(self.bg290, (1440,809))
        # self.bg291 = pygame.transform.scale(self.bg291, (1440,809))
        # self.bg292 = pygame.transform.scale(self.bg292, (1440,809))
        # self.bg293 = pygame.transform.scale(self.bg293, (1440,809))
        # self.bg294 = pygame.transform.scale(self.bg294, (1440,809))
        # self.bg295 = pygame.transform.scale(self.bg295, (1440,809))
        # self.bg296 = pygame.transform.scale(self.bg296, (1440,809))
        # self.bg297 = pygame.transform.scale(self.bg297, (1440,809))
        # self.bg298 = pygame.transform.scale(self.bg298, (1440,809))
        # self.bg299 = pygame.transform.scale(self.bg299, (1440,809))
        # self.bg300 = pygame.transform.scale(self.bg300, (1440,809))
        # self.bg301 = pygame.transform.scale(self.bg301, (1440,809))
        # self.bg302 = pygame.transform.scale(self.bg302, (1440,809))
        # self.bg303 = pygame.transform.scale(self.bg303, (1440,809))
        # self.bg304 = pygame.transform.scale(self.bg304, (1440,809))
        # self.bg305 = pygame.transform.scale(self.bg305, (1440,809))
        # self.bg306 = pygame.transform.scale(self.bg306, (1440,809))
        # self.bg307 = pygame.transform.scale(self.bg307, (1440,809))
        # self.bg308 = pygame.transform.scale(self.bg308, (1440,809))
        # self.bg309 = pygame.transform.scale(self.bg309, (1440,809))
        # self.bg310 = pygame.transform.scale(self.bg310, (1440,809))
        # self.bg311 = pygame.transform.scale(self.bg311, (1440,809))
        # self.bg312 = pygame.transform.scale(self.bg312, (1440,809))
        # self.bg313 = pygame.transform.scale(self.bg313, (1440,809))
        # self.bg314 = pygame.transform.scale(self.bg314, (1440,809))
        # self.bg315 = pygame.transform.scale(self.bg315, (1440,809))
        # self.bg316 = pygame.transform.scale(self.bg316, (1440,809))
        # self.bg317 = pygame.transform.scale(self.bg317, (1440,809))
        # self.bg318 = pygame.transform.scale(self.bg318, (1440,809))
        # self.bg319 = pygame.transform.scale(self.bg319, (1440,809))
        # self.bg320 = pygame.transform.scale(self.bg320, (1440,809))
        # self.bg321 = pygame.transform.scale(self.bg321, (1440,809))
        # self.bg322 = pygame.transform.scale(self.bg322, (1440,809))
        # self.bg323 = pygame.transform.scale(self.bg323, (1440,809))
        # self.bg324 = pygame.transform.scale(self.bg324, (1440,809))
        # self.bg325 = pygame.transform.scale(self.bg325, (1440,809))
        # self.bg326 = pygame.transform.scale(self.bg326, (1440,809))
        # self.bg327 = pygame.transform.scale(self.bg327, (1440,809))
        # self.bg328 = pygame.transform.scale(self.bg328, (1440,809))
        # self.bg329 = pygame.transform.scale(self.bg329, (1440,809))
        # self.bg330 = pygame.transform.scale(self.bg330, (1440,809))
        # self.bg331 = pygame.transform.scale(self.bg331, (1440,809))
        # self.bg332 = pygame.transform.scale(self.bg332, (1440,809))
        # self.bg333 = pygame.transform.scale(self.bg333, (1440,809))
        # self.bg334 = pygame.transform.scale(self.bg334, (1440,809))
        # self.bg335 = pygame.transform.scale(self.bg335, (1440,809))
        # self.bg336 = pygame.transform.scale(self.bg336, (1440,809))
        # self.bg337 = pygame.transform.scale(self.bg337, (1440,809))
        # self.bg338 = pygame.transform.scale(self.bg338, (1440,809))
        # self.bg339 = pygame.transform.scale(self.bg339, (1440,809))
        # self.bg340 = pygame.transform.scale(self.bg340, (1440,809))
        # self.bg341 = pygame.transform.scale(self.bg341, (1440,809))
        # self.bg342 = pygame.transform.scale(self.bg342, (1440,809))
        # self.bg343 = pygame.transform.scale(self.bg343, (1440,809))
        # self.bg344 = pygame.transform.scale(self.bg344, (1440,809))
        # self.bg345 = pygame.transform.scale(self.bg345, (1440,809))
        # self.bg346 = pygame.transform.scale(self.bg346, (1440,809))
        # self.bg347 = pygame.transform.scale(self.bg347, (1440,809))
        # self.bg348 = pygame.transform.scale(self.bg348, (1440,809))
        # self.bg349 = pygame.transform.scale(self.bg349, (1440,809))
        # self.bg350 = pygame.transform.scale(self.bg350, (1440,809))
        # self.bg351 = pygame.transform.scale(self.bg351, (1440,809))
        # self.bg352 = pygame.transform.scale(self.bg352, (1440,809))
        # self.bg353 = pygame.transform.scale(self.bg353, (1440,809))
        # self.bg354 = pygame.transform.scale(self.bg354, (1440,809))
        # self.bg355 = pygame.transform.scale(self.bg355, (1440,809))
        # self.bg356 = pygame.transform.scale(self.bg356, (1440,809))
        # self.bg357 = pygame.transform.scale(self.bg357, (1440,809))
        # self.bg358 = pygame.transform.scale(self.bg358, (1440,809))
        # self.bg359 = pygame.transform.scale(self.bg359, (1440,809))
        # self.bg360 = pygame.transform.scale(self.bg360, (1440,809))
        # self.bg361 = pygame.transform.scale(self.bg361, (1440,809))
        # self.bg362 = pygame.transform.scale(self.bg362, (1440,809))
        # self.bg363 = pygame.transform.scale(self.bg363, (1440,809))
        # self.bg364 = pygame.transform.scale(self.bg364, (1440,809))
        # self.bg365 = pygame.transform.scale(self.bg365, (1440,809))
        # self.bg366 = pygame.transform.scale(self.bg366, (1440,809))
        # self.bg367 = pygame.transform.scale(self.bg367, (1440,809))
        # self.bg368 = pygame.transform.scale(self.bg368, (1440,809))
        # self.bg369 = pygame.transform.scale(self.bg369, (1440,809))
        # self.bg370 = pygame.transform.scale(self.bg370, (1440,809))
        # self.bg371 = pygame.transform.scale(self.bg371, (1440,809))
        # self.bg372 = pygame.transform.scale(self.bg372, (1440,809))
        # self.bg373 = pygame.transform.scale(self.bg373, (1440,809))
        # self.bg374 = pygame.transform.scale(self.bg374, (1440,809))
        # self.bg375 = pygame.transform.scale(self.bg375, (1440,809))
        # self.bg376 = pygame.transform.scale(self.bg376, (1440,809))
        # self.bg377 = pygame.transform.scale(self.bg377, (1440,809))
        # self.bg378 = pygame.transform.scale(self.bg378, (1440,809))
        # self.bg379 = pygame.transform.scale(self.bg379, (1440,809))
        # self.bg380 = pygame.transform.scale(self.bg380, (1440,809))
        # self.bg381 = pygame.transform.scale(self.bg381, (1440,809))
        # self.bg382 = pygame.transform.scale(self.bg382, (1440,809))
        # self.bg383 = pygame.transform.scale(self.bg383, (1440,809))
        # self.bg384 = pygame.transform.scale(self.bg384, (1440,809))
        # self.bg385 = pygame.transform.scale(self.bg385, (1440,809))
        # self.bg386 = pygame.transform.scale(self.bg386, (1440,809))
        # self.bg387 = pygame.transform.scale(self.bg387, (1440,809))
        # self.bg388 = pygame.transform.scale(self.bg388, (1440,809))
        # self.bg389 = pygame.transform.scale(self.bg389, (1440,809))
        # self.bg390 = pygame.transform.scale(self.bg390, (1440,809))
        # self.bg391 = pygame.transform.scale(self.bg391, (1440,809))
        # self.bg392 = pygame.transform.scale(self.bg392, (1440,809))
        # self.bg393 = pygame.transform.scale(self.bg393, (1440,809))
        # self.bg394 = pygame.transform.scale(self.bg394, (1440,809))
        # self.bg395 = pygame.transform.scale(self.bg395, (1440,809))
        # self.bg396 = pygame.transform.scale(self.bg396, (1440,809))
        # self.bg397 = pygame.transform.scale(self.bg397, (1440,809))
        # self.bg398 = pygame.transform.scale(self.bg398, (1440,809))
        # self.bg399 = pygame.transform.scale(self.bg399, (1440,809))
        # self.bg400 = pygame.transform.scale(self.bg400, (1440,809))
        # self.bg401 = pygame.transform.scale(self.bg401, (1440,809))
        # self.bg402 = pygame.transform.scale(self.bg402, (1440,809))
        # self.bg403 = pygame.transform.scale(self.bg403, (1440,809))
        # self.bg404 = pygame.transform.scale(self.bg404, (1440,809))
        # self.bg405 = pygame.transform.scale(self.bg405, (1440,809))
        # self.bg406 = pygame.transform.scale(self.bg406, (1440,809))
        # self.bg407 = pygame.transform.scale(self.bg407, (1440,809))
        # self.bg408 = pygame.transform.scale(self.bg408, (1440,809))
        # self.bg409 = pygame.transform.scale(self.bg409, (1440,809))
        # self.bg410 = pygame.transform.scale(self.bg410, (1440,809))
        # self.bg411 = pygame.transform.scale(self.bg411, (1440,809))
        # self.bg412 = pygame.transform.scale(self.bg412, (1440,809))
        # self.bg413 = pygame.transform.scale(self.bg413, (1440,809))
        # self.bg414 = pygame.transform.scale(self.bg414, (1440,809))
        # self.bg415 = pygame.transform.scale(self.bg415, (1440,809))
        # self.bg416 = pygame.transform.scale(self.bg416, (1440,809))
        # self.bg417 = pygame.transform.scale(self.bg417, (1440,809))
        # self.bg418 = pygame.transform.scale(self.bg418, (1440,809))
        # self.bg419 = pygame.transform.scale(self.bg419, (1440,809))
        # self.bg420 = pygame.transform.scale(self.bg420, (1440,809))
        # self.bg421 = pygame.transform.scale(self.bg421, (1440,809))
        # self.bg422 = pygame.transform.scale(self.bg422, (1440,809))
        # self.bg423 = pygame.transform.scale(self.bg423, (1440,809))
        # self.bg424 = pygame.transform.scale(self.bg424, (1440,809))
        # self.bg425 = pygame.transform.scale(self.bg425, (1440,809))
        # self.bg426 = pygame.transform.scale(self.bg426, (1440,809))
        # self.bg427 = pygame.transform.scale(self.bg427, (1440,809))
        # self.bg428 = pygame.transform.scale(self.bg428, (1440,809))
        # self.bg429 = pygame.transform.scale(self.bg429, (1440,809))
        # self.bg430 = pygame.transform.scale(self.bg430, (1440,809))
        # self.bg431 = pygame.transform.scale(self.bg431, (1440,809))
        # self.bg432 = pygame.transform.scale(self.bg432, (1440,809))
        # self.bg433 = pygame.transform.scale(self.bg433, (1440,809))
        # self.bg434 = pygame.transform.scale(self.bg434, (1440,809))
        # self.bg435 = pygame.transform.scale(self.bg435, (1440,809))
        # self.bg436 = pygame.transform.scale(self.bg436, (1440,809))
        # self.bg437 = pygame.transform.scale(self.bg437, (1440,809))
        # self.bg438 = pygame.transform.scale(self.bg438, (1440,809))
        # self.bg439 = pygame.transform.scale(self.bg439, (1440,809))
        # self.bg440 = pygame.transform.scale(self.bg440, (1440,809))
        # self.bg441 = pygame.transform.scale(self.bg441, (1440,809))
        # self.bg442 = pygame.transform.scale(self.bg442, (1440,809))
        # self.bg443 = pygame.transform.scale(self.bg443, (1440,809))
        # self.bg444 = pygame.transform.scale(self.bg444, (1440,809))
        # self.bg445 = pygame.transform.scale(self.bg445, (1440,809))
        # self.bg446 = pygame.transform.scale(self.bg446, (1440,809))
        # self.bg447 = pygame.transform.scale(self.bg447, (1440,809))
        # self.bg448 = pygame.transform.scale(self.bg448, (1440,809))
        # self.bg449 = pygame.transform.scale(self.bg449, (1440,809))
        # self.bg450 = pygame.transform.scale(self.bg450, (1440,809))
        # self.bg451 = pygame.transform.scale(self.bg451, (1440,809))
        # self.bg452 = pygame.transform.scale(self.bg452, (1440,809))
        # self.bg453 = pygame.transform.scale(self.bg453, (1440,809))
        # self.bg454 = pygame.transform.scale(self.bg454, (1440,809))
        # self.bg455 = pygame.transform.scale(self.bg455, (1440,809))
        # self.bg456 = pygame.transform.scale(self.bg456, (1440,809))
        # self.bg457 = pygame.transform.scale(self.bg457, (1440,809))
        # self.bg458 = pygame.transform.scale(self.bg458, (1440,809))
        # self.bg459 = pygame.transform.scale(self.bg459, (1440,809))
        # self.bg460 = pygame.transform.scale(self.bg460, (1440,809))
        # self.bg461 = pygame.transform.scale(self.bg461, (1440,809))
        # self.bg462 = pygame.transform.scale(self.bg462, (1440,809))
        # self.bg463 = pygame.transform.scale(self.bg463, (1440,809))
        # self.bg464 = pygame.transform.scale(self.bg464, (1440,809))
        # self.bg465 = pygame.transform.scale(self.bg465, (1440,809))
        # self.bg466 = pygame.transform.scale(self.bg466, (1440,809))
        # self.bg467 = pygame.transform.scale(self.bg467, (1440,809))
        # self.bg468 = pygame.transform.scale(self.bg468, (1440,809))
        # self.bg469 = pygame.transform.scale(self.bg469, (1440,809))
        # self.bg470 = pygame.transform.scale(self.bg470, (1440,809))
        # self.bg471 = pygame.transform.scale(self.bg471, (1440,809))
        # self.bg472 = pygame.transform.scale(self.bg472, (1440,809))
        # self.bg473 = pygame.transform.scale(self.bg473, (1440,809))
        # self.bg474 = pygame.transform.scale(self.bg474, (1440,809))
        # self.bg475 = pygame.transform.scale(self.bg475, (1440,809))
        # self.bg476 = pygame.transform.scale(self.bg476, (1440,809))
        # self.bg477 = pygame.transform.scale(self.bg477, (1440,809))
        # self.bg478 = pygame.transform.scale(self.bg478, (1440,809))
        # self.bg479 = pygame.transform.scale(self.bg479, (1440,809))
        # self.bg480 = pygame.transform.scale(self.bg480, (1440,809))
        # self.bg481 = pygame.transform.scale(self.bg481, (1440,809))
        # self.bg482 = pygame.transform.scale(self.bg482, (1440,809))
        # self.bg483 = pygame.transform.scale(self.bg483, (1440,809))
        # self.bg484 = pygame.transform.scale(self.bg484, (1440,809))
        # self.bg485 = pygame.transform.scale(self.bg485, (1440,809))
        # self.bg486 = pygame.transform.scale(self.bg486, (1440,809))
        # self.bg487 = pygame.transform.scale(self.bg487, (1440,809))
        # self.bg488 = pygame.transform.scale(self.bg488, (1440,809))
        # self.bg489 = pygame.transform.scale(self.bg489, (1440,809))
        # self.bg490 = pygame.transform.scale(self.bg490, (1440,809))
        # self.bg491 = pygame.transform.scale(self.bg491, (1440,809))
        # self.bg492 = pygame.transform.scale(self.bg492, (1440,809))
        # self.bg493 = pygame.transform.scale(self.bg493, (1440,809))
        # self.bg494 = pygame.transform.scale(self.bg494, (1440,809))
        # self.bg495 = pygame.transform.scale(self.bg495, (1440,809))
        # self.bg496 = pygame.transform.scale(self.bg496, (1440,809))
        # self.bg497 = pygame.transform.scale(self.bg497, (1440,809))
        # self.bg498 = pygame.transform.scale(self.bg498, (1440,809))
        # self.bg499 = pygame.transform.scale(self.bg499, (1440,809))
        # self.bg500 = pygame.transform.scale(self.bg500, (1440,809))
        # self.bg501 = pygame.transform.scale(self.bg501, (1440, 809))
        # self.bg502 = pygame.transform.scale(self.bg502, (1440, 809))
        # self.bg503 = pygame.transform.scale(self.bg503, (1440, 809))
        # self.bg504 = pygame.transform.scale(self.bg504, (1440, 809))
        # self.bg505 = pygame.transform.scale(self.bg505, (1440, 809))
        # self.bg506 = pygame.transform.scale(self.bg506, (1440, 809))
        # self.bg507 = pygame.transform.scale(self.bg507, (1440, 809))
        # self.bg508 = pygame.transform.scale(self.bg508, (1440, 809))
        # self.bg509 = pygame.transform.scale(self.bg509, (1440, 809))
        # self.bg510 = pygame.transform.scale(self.bg510, (1440, 809))
        # self.bg511 = pygame.transform.scale(self.bg511, (1440, 809))
        # self.bg512 = pygame.transform.scale(self.bg512, (1440, 809))
        # self.bg513 = pygame.transform.scale(self.bg513, (1440, 809))
        # self.bg514 = pygame.transform.scale(self.bg514, (1440, 809))
        # self.bg515 = pygame.transform.scale(self.bg515, (1440, 809))
        # self.bg516 = pygame.transform.scale(self.bg516, (1440, 809))
        # self.bg517 = pygame.transform.scale(self.bg517, (1440, 809))
        # self.bg518 = pygame.transform.scale(self.bg518, (1440, 809))
        # self.bg519 = pygame.transform.scale(self.bg519, (1440, 809))
        # self.bg520 = pygame.transform.scale(self.bg520, (1440, 809))
        # self.bg521 = pygame.transform.scale(self.bg521, (1440, 809))
        # self.bg522 = pygame.transform.scale(self.bg522, (1440, 809))
        # self.bg523 = pygame.transform.scale(self.bg523, (1440, 809))
        # self.bg524 = pygame.transform.scale(self.bg524, (1440, 809))
        # self.bg525 = pygame.transform.scale(self.bg525, (1440, 809))
        # self.bg526 = pygame.transform.scale(self.bg526, (1440, 809))
        # self.bg527 = pygame.transform.scale(self.bg527, (1440, 809))
        # self.bg528 = pygame.transform.scale(self.bg528, (1440, 809))
        # self.bg529 = pygame.transform.scale(self.bg529, (1440, 809))
        # self.bg530 = pygame.transform.scale(self.bg530, (1440, 809))
        # self.bg531 = pygame.transform.scale(self.bg531, (1440, 809))
        # self.bg532 = pygame.transform.scale(self.bg532, (1440, 809))
        # self.bg533 = pygame.transform.scale(self.bg533, (1440, 809))
        # self.bg534 = pygame.transform.scale(self.bg534, (1440, 809))
        # self.bg535 = pygame.transform.scale(self.bg535, (1440, 809))
        # self.bg536 = pygame.transform.scale(self.bg536, (1440, 809))
        # self.bg537 = pygame.transform.scale(self.bg537, (1440, 809))
        # self.bg538 = pygame.transform.scale(self.bg538, (1440, 809))
        # self.bg539 = pygame.transform.scale(self.bg539, (1440, 809))
        # self.bg540 = pygame.transform.scale(self.bg540, (1440, 809))
        # self.bg541 = pygame.transform.scale(self.bg541, (1440, 809))
        # self.bg542 = pygame.transform.scale(self.bg542, (1440, 809))
        # self.bg543 = pygame.transform.scale(self.bg543, (1440, 809))
        # self.bg544 = pygame.transform.scale(self.bg544, (1440, 809))
        # self.bg545 = pygame.transform.scale(self.bg545, (1440, 809))
        # self.bg546 = pygame.transform.scale(self.bg546, (1440, 809))
        # self.bg547 = pygame.transform.scale(self.bg547, (1440, 809))
        # self.bg548 = pygame.transform.scale(self.bg548, (1440, 809))
        # self.bg549 = pygame.transform.scale(self.bg549, (1440, 809))
        # self.bg550 = pygame.transform.scale(self.bg550, (1440, 809))
        # self.bg551 = pygame.transform.scale(self.bg551, (1440, 809))
        # self.bg552 = pygame.transform.scale(self.bg552, (1440, 809))
        # self.bg553 = pygame.transform.scale(self.bg553, (1440, 809))
        # self.bg554 = pygame.transform.scale(self.bg554, (1440, 809))
        # self.bg555 = pygame.transform.scale(self.bg555, (1440, 809))
        # self.bg556 = pygame.transform.scale(self.bg556, (1440, 809))
        # self.bg557 = pygame.transform.scale(self.bg557, (1440, 809))
        # self.bg558 = pygame.transform.scale(self.bg558, (1440, 809))
        # self.bg559 = pygame.transform.scale(self.bg559, (1440, 809))
        # self.bg560 = pygame.transform.scale(self.bg560, (1440, 809))
        # self.bg561 = pygame.transform.scale(self.bg561, (1440, 809))
        # self.bg562 = pygame.transform.scale(self.bg562, (1440, 809))
        # self.bg563 = pygame.transform.scale(self.bg563, (1440, 809))
        # self.bg564 = pygame.transform.scale(self.bg564, (1440, 809))
        # self.bg565 = pygame.transform.scale(self.bg565, (1440, 809))
        # self.bg566 = pygame.transform.scale(self.bg566, (1440, 809))
        # self.bg567 = pygame.transform.scale(self.bg567, (1440, 809))
        # self.bg568 = pygame.transform.scale(self.bg568, (1440, 809))
        # self.bg569 = pygame.transform.scale(self.bg569, (1440, 809))
        # self.bg570 = pygame.transform.scale(self.bg570, (1440, 809))
        # self.bg571 = pygame.transform.scale(self.bg571, (1440, 809))
        # self.bg572 = pygame.transform.scale(self.bg572, (1440, 809))
        # self.bg573 = pygame.transform.scale(self.bg573, (1440, 809))
        # self.bg574 = pygame.transform.scale(self.bg574, (1440, 809))
        # self.bg575 = pygame.transform.scale(self.bg575, (1440, 809))
        # self.bg576 = pygame.transform.scale(self.bg576, (1440, 809))
        # self.bg577 = pygame.transform.scale(self.bg577, (1440, 809))
        # self.bg578 = pygame.transform.scale(self.bg578, (1440, 809))
        # self.bg579 = pygame.transform.scale(self.bg579, (1440, 809))
        # self.bg580 = pygame.transform.scale(self.bg580, (1440, 809))
        # self.bg581 = pygame.transform.scale(self.bg581, (1440, 809))
        # self.bg582 = pygame.transform.scale(self.bg582, (1440, 809))
        # self.bg583 = pygame.transform.scale(self.bg583, (1440, 809))
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
            self.bg242,
            self.bg243,
            self.bg244,
            self.bg245,
            self.bg246,
            self.bg247,
            self.bg248,
            self.bg249,
            self.bg250,
            self.bg251,
            self.bg252,
            self.bg253,
            self.bg254,
            self.bg255,
            self.bg256,
            self.bg257,
            self.bg258,
            self.bg259,
            self.bg260,
            self.bg261,
            self.bg262,
            self.bg263,
            self.bg264,
            self.bg265,
            self.bg266,
            self.bg267,
            self.bg268,
            self.bg269,
            self.bg270,
            self.bg271,
            self.bg272,
            self.bg273,
            self.bg274,
            self.bg275,
            self.bg276,
            self.bg277,
            self.bg278,
            self.bg279,
            self.bg280,
            self.bg281,
            self.bg282,
            self.bg283,
            self.bg284,
            self.bg285,
            self.bg286,
            self.bg287,
            self.bg288,
            self.bg289,
            self.bg290,
            self.bg291,
            self.bg292,
            self.bg293,
            self.bg294,
            self.bg295,
            self.bg296,
            self.bg297,
            self.bg298,
            self.bg299,
            self.bg300,
            self.bg301,
            self.bg302,
            self.bg303,
            self.bg304,
            self.bg305,
            self.bg306,
            self.bg307,
            self.bg308,
            self.bg309,
            self.bg310,
            self.bg311,
            self.bg312,
            self.bg313,
            self.bg314,
            self.bg315,
            self.bg316,
            self.bg317,
            self.bg318,
            self.bg319,
            self.bg320,
            self.bg321,
            self.bg322,
            self.bg323,
            self.bg324,
            self.bg325,
            self.bg326,
            self.bg327,
            self.bg328,
            self.bg329,
            self.bg330,
            self.bg331,
            self.bg332,
            self.bg333,
            self.bg334,
            self.bg335,
            self.bg336,
            self.bg337,
            self.bg338,
            self.bg339,
            self.bg340,
            self.bg341,
            self.bg342,
            self.bg343,
            self.bg344,
            self.bg345,
            self.bg346,
            self.bg347,
            self.bg348,
            self.bg349,
            self.bg350,
            self.bg351,
            self.bg352,
            self.bg353,
            self.bg354,
            self.bg355,
            self.bg356,
            self.bg357,
            self.bg358,
            self.bg359,
            self.bg360,
            self.bg361,
            self.bg362,
            self.bg363,
            self.bg364,
            self.bg365,
            self.bg366,
            self.bg367,
            self.bg368,
            self.bg369,
            self.bg370,
            self.bg371,
            self.bg372,
            self.bg373,
            self.bg374,
            self.bg375,
            self.bg376,
            self.bg377,
            self.bg378,
            self.bg379,
            self.bg380,
            self.bg381,
            self.bg382,
            self.bg383,
            self.bg384,
            self.bg385,
            self.bg386,
            self.bg387,
            self.bg388,
            self.bg389,
            self.bg390,
            self.bg391,
            self.bg392,
            self.bg393,
            self.bg394,
            self.bg395,
            self.bg396,
            self.bg397,
            self.bg398,
            self.bg399,
            self.bg400,
            self.bg401,
            self.bg402,
            self.bg403,
            self.bg404,
            self.bg405,
            self.bg406,
            self.bg407,
            self.bg408,
            self.bg409,
            self.bg410,
            self.bg411,
            self.bg412,
            self.bg413,
            self.bg414,
            self.bg415,
            self.bg416,
            self.bg417,
            self.bg418,
            self.bg419,
            self.bg420,
            self.bg421,
            self.bg422,
            self.bg423,
            self.bg424,
            self.bg425,
            self.bg426,
            self.bg427,
            self.bg428,
            self.bg429,
            self.bg430,
            self.bg431,
            self.bg432,
            self.bg433,
            self.bg434,
            self.bg435,
            self.bg436,
            self.bg437,
            self.bg438,
            self.bg439,
            self.bg440,
            self.bg441,
            self.bg442,
            self.bg443,
            self.bg444,
            self.bg445,
            self.bg446,
            self.bg447,
            self.bg448,
            self.bg449,
            self.bg450,
            self.bg451,
            self.bg452,
            self.bg453,
            self.bg454,
            self.bg455,
            self.bg456,
            self.bg457,
            self.bg458,
            self.bg459,
            self.bg460,
            self.bg461,
            self.bg462,
            self.bg463,
            self.bg464,
            self.bg465,
            self.bg466,
            self.bg467,
            self.bg468,
            self.bg469,
            self.bg470,
            self.bg471,
            self.bg472,
            self.bg473,
            self.bg474,
            self.bg475,
            self.bg476,
            self.bg477,
            self.bg478,
            self.bg479,
            self.bg480,
            self.bg481,
            self.bg482,
            self.bg483,
            self.bg484,
            self.bg485,
            self.bg486,
            self.bg487,
            self.bg488,
            self.bg489,
            self.bg490,
            self.bg491,
            self.bg492,
            self.bg493,
            self.bg494,
            self.bg495,
            self.bg496,
            self.bg497,
            self.bg498,
            self.bg499,
            self.bg500,
            self.bg501,
            self.bg502,
            self.bg503,
            self.bg504,
            self.bg505,
            self.bg506,
            self.bg507,
            self.bg508,
            self.bg509,
            self.bg510,
            self.bg511,
            self.bg512,
            self.bg513,
            self.bg514,
            self.bg515,
            self.bg516,
            self.bg517,
            self.bg518,
            self.bg519,
            self.bg520,
            self.bg521,
            self.bg522,
            self.bg523,
            self.bg524,
            self.bg525,
            self.bg526,
            self.bg527,
            self.bg528,
            self.bg529,
            self.bg530,
            self.bg531,
            self.bg532,
            self.bg533,
            self.bg534,
            self.bg535,
            self.bg536,
            self.bg537,
            self.bg538,
            self.bg539,
            self.bg540,
            self.bg541,
            self.bg542,
            self.bg543,
            self.bg544,
            self.bg545,
            self.bg546,
            self.bg547,
            self.bg548,
            self.bg549,
            self.bg550,
            self.bg551,
            self.bg552,
            self.bg553,
            self.bg554,
            self.bg555,
            self.bg556,
            self.bg557,
            self.bg558,
            self.bg559,
            self.bg560,
            self.bg561,
            self.bg562,
            self.bg563,
            self.bg564,
            self.bg565,
            self.bg566,
            self.bg567,
            self.bg568,
            self.bg569,
            self.bg570,
            self.bg571,
            self.bg572,
            self.bg573,
            self.bg574,
            self.bg575,
            self.bg576,
            self.bg577,
            self.bg578,
            self.bg579,
            self.bg580,
            self.bg581,
            self.bg582,
            self.bg583
        ]
        self.FPS = 20
        self.frame_per_second = pygame.time.Clock()


    def play_intro(self):
        pygame.mixer.music.load("song/main_menu_theme.ogg")
        pygame.mixer.music.play(0)
        self.run_intro = True
        while self.run_intro:
            self.game.display.blit(self.frame[self.number], self.bg_rect)
            self.number += 1
            if self.number == 159:
                self.FPS = 15
            if self.number == 583:
                self.run_intro = False
                self.game.curr_menu.display_menu()
            self.check_event()
            self.game.main_menu.update_screen()
            self.frame_per_second.tick(self.FPS)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.run_intro = False
                self.game.curr_menu.display_menu()

