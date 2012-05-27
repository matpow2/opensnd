# Copyright (c) Mathias Kaerlev 2012.

# This file is part of OpenSND.

# OpenSND is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# OpenSND is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with OpenSND.  If not, see <http://www.gnu.org/licenses/>.

from common import *
from objects import *
from images import *
from fonts import *
from sounds import *
from PySide.QtCore import Qt
import os

qualifier_1 = (SpawnArea_192, Tree_260, Rock_264, DeadTree_265,
    GroundBackground_266, Stone_267, House_271, Sidewalk_272,
    BrokenSidewalk_273, Street_274, PoliceCar_275, PoliceCar2_276,
    Stone2_277, Tree3_278, Street2_279, Sidewalk2_280, Crossroad_281,
    Rock3_282, Rock3_283, Rock4_284, Skeleton_285, Bush_286, Box_287,
    DestroyedBox_288, Gate_289, Bush2_290, Boulders_291, Cactus_292,
    SmallCactus_293, Stone3_294, Tombstone_295, Floor_296, Floor2_297,
    WoodenFloor_298, StoneFloor_299, Wall11_300, Wall12_301, Wall21_302,
    Wall22_303, Tree3_304, Pond_305, Rubble_327, Skeleton2_328,
    Entrance_329, Lantern_330, BurningBox_331, PoliceSpawn_345,
    TerrorSpawn_346, Hill_402, Pipeline_403, FenceHor_404, FenceVert_405,
    BrokenPipeline_406, Wall13_407, Wall14_408, Wall23_409, Wall24_410,
    PipelineDestroyed_411, Grass2_414, Desert2_415, Dust2_416)

qualifier_2 = (Tree_260, Rock_264, DeadTree_265, Stone_267, House_271,
    PoliceCar_275, PoliceCar2_276, Stone2_277, Tree3_278, Rock3_282,
    Rock3_283, Rock4_284, Bush_286, Box_287, Gate_289, Bush2_290,
    Cactus_292, SmallCactus_293, Stone3_294, Tombstone_295, Tree3_304,
    Rubble_327, Entrance_329, Lantern_330, BurningBox_331, Hill_402,
    Pipeline_403, FenceHor_404, FenceVert_405)

qualifier_3 = (DeadTree_265, Tree3_278, Stone3_294, Wall11_300,
    Wall12_301, Wall21_302, Wall22_303, Pond_305, Pipeline_403,
    Wall13_407, Wall14_408, Wall23_409, Wall24_410)

qualifier_5 = (Obj1Weapon_308, Obj2Weapon_309, AmmoText_310, _313,
    Obj1WeaponList_314, Obj2WeaponList_315, PlOnlineText_316, Cash_364,
    _365, Score_367, HealthText_401, Obj1WeaponList_481, Skin_483)

qualifier_6 = (Wall11_300, Wall12_301, Wall21_302, Wall22_303,
    Wall13_407, Wall14_408, Wall23_409, Wall24_410)

qualifier_7 = (Up2_418, Right2_419, Down2_420, Left2_421)

qualifier_8 = (Obj2Die_199, Obj1Die_255, Obj3Die_338, Obj4Die_339,
    Obj5Die_340, Obj6Die_341)

qualifier_99 = (GroundBackground_266, Sidewalk_272,
    BrokenSidewalk_273, Street_274, Street2_279, Sidewalk2_280,
    Crossroad_281, Floor_296, Floor2_297, WoodenFloor_298, StoneFloor_299,
    Grass2_414, Desert2_415, Dust2_416)

DISPLAY_CLASSES = [GroundBackground_266, Dust2_416, Desert2_415,
                 Grass2_414, Street_274, Street2_279,
                 Crossroad_281, Sidewalk_272, BrokenSidewalk_273,
                 Sidewalk2_280, Skeleton_285, Floor_296,
                 Floor2_297, WoodenFloor_298, StoneFloor_299,
                 BrokenPipeline_406, DestroyedBox_288,
                 Boulders_291, Skeleton2_328]

DISPLAY_IDS = {
    -1 : SpawnArea_192,
    -2 : PoliceSpawn_345,
    -3 : TerrorSpawn_346,
    1 : Tree_260,
    2 : Rock_264,
    3 : GroundBackground_266,
    4 : Stone_267,
    5 : DeadTree_265,
    6 : House_271,
    7 : Sidewalk_272,
    8 : BrokenSidewalk_273,
    9 : Street_274,
    10 : PoliceCar_275,
    11 : PoliceCar2_276,
    12 : Stone2_277,
    13 : Tree3_278,
    14 : Street2_279,
    15 : Sidewalk2_280,
    16 : Crossroad_281,
    17 : Rock3_282,
    18 : Rock3_283,
    19 : Rock4_284,
    20 : Skeleton_285,
    21 : Bush_286,
    22 : Box_287,
    23 : DestroyedBox_288,
    24 : Gate_289,
    25 : Bush2_290,
    26 : Boulders_291,
    27 : Cactus_292,
    28 : SmallCactus_293,
    29 : Stone3_294,
    30 : Tombstone_295,
    31 : Floor_296,
    32 : Floor2_297,
    33 : WoodenFloor_298,
    34 : StoneFloor_299,
    35 : Wall11_300,
    36 : Wall12_301,
    37 : Wall21_302,
    38 : Wall22_303,
    39 : Tree3_304,
    40 : Pond_305,
    41 : Rubble_327,
    42 : Skeleton2_328,
    43 : Entrance_329,
    44 : Lantern_330,
    45 : BurningBox_331,
    46 : Hill_402,
    47 : Pipeline_403,
    48 : FenceHor_404,
    49 : FenceVert_405,
    50 : BrokenPipeline_406,
    51 : Grass2_414,
    52 : Desert2_415,
    53 : Dust2_416,
    54 : Wall13_407,
    55 : Wall14_408,
    56 : Wall23_409,
    57 : Wall24_410
}

class Frame6(Frame):
    name = 'Game'
    index = 5
    width = 800
    height = 600
    background = (0, 0, 0)
    
    def initialize(self):
        self.create_object(OverlayRedux2_443, 0, 0)
        self.create_object(CheckKick_216, 24, -106)
        self.create_object(ErrorMsg_244, 231, -167)
        self.create_object(ChosedMap_125, -174, 300)
        self.create_object(ChosedMapWithoutPath_126, -182, 283)
        self.create_object(MessageOfDay_58, -135, -128)
        self.create_object(WeaponAllowed_59, -139, -99)
        self.create_object(ServerError_60, -129, -84)
        self.create_object(CheckDaMap_176, 437, -167)
        self.create_object(RealName_390, 621, -154)
        self.create_object(ClanTag_65, 30, -42)
        self.create_object(SvrPw_155, 654, 624)
        self.create_object(BanList_393, 89, 734)
        self.create_object(Checkip_395, 87, 771)
        self.create_object(Mapid_397, 670, 729)
        self.create_object(Msg_427, 7, 611)
        self.create_object(Svrmotd_428, 293, 623)
        self.create_object(Sting_186, -219, 42)
        self.create_object(Temp_431, -246, 188)
        self.create_object(String31_437, 727, 710)
        self.create_object(Sall_446, 613, 790)
        self.create_object(Msg2_449, -246, 208)
        self.create_object(Temp2_454, -243, 226)
        self.create_object(Shop1Blitter3_386, 441, 269)
        self.create_object(Shop1Blitter2_385, 268, 269)
        self.create_object(StringParser_43, 268, -69)
        self.create_object(Fusssoldat_193, 507, 620)
        self.create_object(Fusssoldat2_194, 543, 622)
        self.create_object(Active7_195, 65, -21)
        self.create_object(Active8_196, 63, -13)
        self.create_object(Rauch_197, 138, -35)
        self.create_object(HitBack_198, 85, -25)
        self.create_object(Frags_209, -35, -6)
        self.create_object(Deaths_210, -31, 10)
        self.create_object(SkillCounter_211, 393, -52)
        self.create_object(GlobalName_6, 71, -89)
        self.create_object(ServerName_100, 299, -100)
        self.create_object(MaxPlayer_102, 480, -30)
        self.create_object(Active6_214, 475, 28)
        self.create_object(Gaswolke_215, 543, -99)
        self.create_object(Version_26, 314, -79)
        self.create_object(Ip_46, 62, -162)
        self.create_object(Port_47, 61, -139)
        self.create_object(ActiveObject1_218, 412, 622)
        self.create_object(Message1_205, 11, 493)
        self.create_object(Message2_206, 11, 510)
        self.create_object(Message3_207, 11, 527)
        self.create_object(Respawn_201, 461, 414)
        self.create_object(Strafing_219, 196, -24)
        self.create_object(Ip2_9, 323, -147)
        self.create_object(Port2_10, 322, -126)
        self.create_object(ExitCounter_221, 129, -136)
        self.create_object(Active9_222, 299, 243)
        self.create_object(Mouse_224, 229, 516)
        self.create_object(Left_225, 204, 516)
        self.create_object(Right_226, 255, 516)
        self.create_object(Up_227, 143, 517)
        self.create_object(Down_228, 143, 568)
        self.create_object(Mouse2_229, 142, 542)
        self.create_object(ShotLatence_230, 187, -147)
        self.create_object(PingCounter_232, 24, -128)
        self.create_object(Ping_233, 25, -89)
        self.create_object(ScoreBar_234, 400, 137)
        self.create_object(FragsScore_236, 363, 158)
        self.create_object(IdScore_237, 439, 158)
        self.create_object(Accuracy_238, 401, -142)
        self.create_object(Oben_239, 251, 619)
        self.create_object(Unten_240, 253, 637)
        self.create_object(Rechts_241, 265, 628)
        self.create_object(Links_242, 245, 628)
        self.create_object(Message4_243, 11, 544)
        self.create_object(DurchlaufChat_245, 396, -102)
        self.create_object(NameScore_235, 232, 158)
        self.create_object(Counter3_246, 468, 619)
        self.create_object(Exp_247, 462, -110)
        self.create_object(FastMouse_252, 372, -167)
        self.create_object(Blood3_253, 577, 624)
        self.create_object(Active2_254, 442, 653)
        self.create_object(BackgroundX_261, 1031, 392)
        self.create_object(BackgroundY_262, 1031, 442)
        self.create_object(TrackX_268, 629, 639)
        self.create_object(TrackY_269, 629, 664)
        self.create_object(Track_270, 672, 660)
        self.create_object(IdPing_307, 504, 158)
        self.create_object(Obj1Weapon_308, 59, 13)
        self.create_object(Obj2Weapon_309, 55, 30)
        self.create_object(AmmoText_310, 281, 12)
        self.create_object(AmmoCurrent_311, 343, 18)
        self.create_object(AmmoFull_312, 385, 18)
        self.create_object(_313, 351, 12)
        self.create_object(Obj1WeaponList_314, 110, 7)
        self.create_object(Obj2WeaponList_315, 110, 24)
        self.create_object(PlOnlineText_316, 381, 108)
        self.create_object(Players_317, 494, 114)
        self.create_object(SecondWeapon_318, -16, -33)
        self.create_object(Ammo1_321, -86, -43)
        self.create_object(Ammo2_322, -85, -13)
        self.create_object(Reload2_323, -57, -19)
        self.create_object(Sleep_324, -16, -113)
        self.create_object(ChangeMap_217, 22, 453)
        self.create_object(DetectMouseChange_325, 134, 672)
        self.create_object(SaveMouseChange_326, 195, 672)
        self.create_object(RemoteIP_20, 537, -154)
        self.create_object(HostIP_150, 152, -188)
        self.create_object(EigeneIP_21, 521, -166)
        self.create_object(Stone_267, 295, -129)
        self.create_object(String2_200, 326, 395)
        self.create_object(MsgCounter_332, -60, 100)
        self.create_object(FlameDie_333, -55, 204)
        self.create_object(Player_334, -364, 509)
        self.create_object(MooSock_335, 511, 657)
        self.create_object(Mode_344, 851, 167)
        self.create_object(PoliceSpawn_345, 77, -50)
        self.create_object(TerrorSpawn_346, 50, -54)
        self.create_object(NameScore2_347, 232, 158)
        self.create_object(FragsScore2_348, 363, 158)
        self.create_object(IdScore2_349, 439, 158)
        self.create_object(IdPing2_350, 504, 158)
        self.create_object(NameScore3_351, 232, 158)
        self.create_object(FragsScore3_352, 363, 158)
        self.create_object(IdScore3_353, 439, 158)
        self.create_object(IdPing3_354, 504, 158)
        self.create_object(Police_342, 512, 9)
        self.create_object(Terror_343, 512, 31)
        self.create_object(ChattingPlayer_356, 158, 636)
        self.create_object(Police2_357, 831, 8)
        self.create_object(Terror2_358, 831, 40)
        self.create_object(PoliceLeft_359, 831, 72)
        self.create_object(TerrorLeft_360, 831, 104)
        self.create_object(RoundStart_361, 831, 136)
        self.create_object(PoliceWin_362, -113, 673)
        self.create_object(TerrorWin_363, -124, 708)
        self.create_object(Cash_364, 77, 46)
        self.create_object(_365, 178, 47)
        self.create_object(Score_367, 761, 12)
        self.create_object(ScorePolice_368, 788, 34)
        self.create_object(ScoreTerror_369, 788, 50)
        self.create_object(Killed_203, 140, 55)
        self.create_object(Money_366, 166, 52)
        self.create_object(ShopList_370, 859, 523)
        self.create_object(ShopListPrice_371, 991, 525)
        self.create_object(Shop1Blitter_372, 266, 268)
        self.create_object(Shop2Blitter_373, 439, 268)
        self.create_object(FlashTime_381, -74, 288)
        self.create_object(PlShadow_382, 621, 751)
        self.create_object(XtraXtraCRC_182, -74, 138)
        self.create_object(CheckFlash_387, 766, -46)
        self.create_object(InvincibleTime_388, 496, -66)
        self.create_object(TurningSpeed_389, 357, -123)
        self.create_object(ModMusic_391, 594, -52)
        self.create_object(Respawntext_392, 253, 395)
        self.create_object(ScreenshotNr_23, 204, 719)
        self.create_object(Banid_396, 38, 753)
        self.create_object(Shooting_399, 717, 621)
        self.create_object(HP_400, 338, 25)
        self.create_object(HealthText_401, 292, 29)
        self.create_object(DM_412, 896, 167)
        self.create_object(Modestatus_413, 946, 165)
        self.create_object(GlobalValues_165, -65, 242)
        self.create_object(Up2_418, -190, 161)
        self.create_object(Right2_419, -189, 164)
        self.create_object(Down2_420, -189, 165)
        self.create_object(Left2_421, -194, 165)
        self.create_object(VisibleId_424, 788, 627)
        self.create_object(IdAllocation_425, 771, 670)
        self.create_object(SvrKills2_32, -97, 85)
        self.create_object(SvrDeaths2_33, -100, 107)
        self.create_object(SvrPoints2_34, -100, 126)
        self.create_object(Moo_181, -202, 323)
        self.create_object(NotID_430, -133, 201)
        self.create_object(Csm_432, -164, 105)
        self.create_object(Counter_434, 340, 27)
        self.create_object(Cp2c_436, 169, 767)
        self.create_object(Snipercounter_438, -209, 422)
        self.create_object(Counter2_439, 340, 27)
        self.create_object(Counter4_440, 340, 27)
        self.create_object(Head_441, 134, -69)
        self.create_object(Follower_442, 400, 300)
        self.create_object(Watersplosh_444, -135, 265)
        self.create_object(BinaryObject_38, 606, -176)
        self.create_object(Moo2_447, -222, 367)
        self.create_object(Dir_455, -158, -7)
        self.create_object(Chat_204, 182, 567)
        self.create_object(Ini_55, 579, -141)
        self.create_object(ScoreBoard_231, -162, 344)
        self.create_object(LoadMap_259, 825, 390)
        self.create_object(WeaponList_320, 817, 227)
        self.create_object(Edit2_336, 264, 675)
        self.create_object(Mapcycle_417, -165, 492)
        self.create_object(Reclist_426, 457, 712)
        self.create_object(Timeout1_448, -171, 175)
        self.add_timed_call(self.on_timer_1, 20.0)
        self.add_timed_call(self.on_timer_2, 10.0)
        self.groups = {
            'Footsteps' : False,
            'Server' : False,
            'W 11' : False,
            'Con' : True,
            'Msg' : False,
            'Load Map' : False,
            'Both' : True,
            'Flashed' : False,
            'Join Team' : False,
            'Map change' : False,
            'Weapon Change Normal' : False,
            'Grenades' : False,
            'Game' : True,
            'Mapcycle' : False,
            'W1' : True,
            'W 8' : False,
            'Connect' : False,
            'W 10' : False,
            'Crates' : False,
            'Add server' : False,
            'Dead Reckoning' : True,
            'W2' : False,
            'Speed Hack' : False,
            'Server main' : False,
            'Graphic reduced 3' : False,
            'Custom Movement' : True,
            'Disconnect' : False,
            'Overlayer' : False,
            'W 6' : False,
            'User left' : False,
            'Client' : False,
            'Shop' : False,
            'W 7' : False,
            'W 12' : False,
            'Graphic reduced' : False,
            'Weapon Change' : False,
            'Music' : False,
            'W 4' : False,
            'W 5' : False,
            'W3' : False,
            'Reload' : False,
            'Server Player' : False,
            'Timer' : False,
            'Layer' : False,
            'Background' : False,
            'W 9' : False,
            'Change team respawn dm' : False,
            'Client main' : False,
            'Backfix' : False,
            'Mapcycle active' : False,
            'Graphic reduced 2' : False,
            'Chat' : False,
            'reset standard' : False,
            'Server other Player' : False,
        }
    
    def on_start(self):
        self.set_event_id(1)
        if select(self.get(GlobalValues_165).values.get(4, 0) == 1):
            self.get(MooSock_335).destroy()
        self.set_event_id(2)
        self.values[3] = 0
        self.values[14] = 0
        self.values[15] = 0
        self.get(HP_400).values[9] = 9999999
        self.get(Moo_181).set_timeout(7000)
        self.get(Moo2_447).set_timeout(7000)
        self.audio.set_default_directory('Sounds\\')
        self.set_event_id(3)
        self.players[0].set_ignore(True)
        self.get(StringParser_43).add_delimiter(',')
        self.players[0].lives = 1+7*self.get_global_value(9)
        self.get(Active7_195).destroy()
        self.get(Fusssoldat_193).values[19] = 0
        self.groups['Weapon Change'] = True
        self.get(Active8_196).destroy()
        self.values[3] = 0
        self.get(Fusssoldat_193).values[8] = 0
        self.get(Ini_55).set_filename(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'data.ini')
        self.get(Ini_55).set_group('Data')
        self.players[1].up = key_from_name(self.get(Ini_55).get_string_item('Up'))
        self.players[1].down = key_from_name(self.get(Ini_55).get_string_item('Down'))
        self.players[1].left = key_from_name(self.get(Ini_55).get_string_item('Left'))
        self.players[1].right = key_from_name(self.get(Ini_55).get_string_item('Right'))
        self.players[2].fire1 = key_from_name(self.get(Ini_55).get_string_item('Reload'))
        self.players[2].fire1 = key_from_name(self.get(Ini_55).get_string_item('Switch'))
        self.players[2].up = key_from_name(self.get(Ini_55).get_string_item('AimH'))
        self.get(Fusssoldat_193).values[0] = 0
        self.get(Fusssoldat2_194).destroy()
        self.get(Fusssoldat_193).values[12] = 0
        self.get(Oben_239).values[9] = 10000005
        self.get(ScoreBar_234).values[9] = 10000010
        for item in self.get(qualifier_5, True):
            item.values[9] = 10000009
        self.get(Active6_214).values[9] = 10000009
        self.get(AmmoCurrent_311).set_value(1)
        self.hide_cursor()
        for item in self.get(SpawnArea_192, True):
            item.destroy()
        self.get(Player_334).values[9] = 9999999
        # self.stop_timer(0)
        self.get(PoliceSpawn_345).destroy()
        self.get(TerrorSpawn_346).destroy()
        self.get(Unten_240).values[9] = 10000002
        self.get(Rechts_241).values[9] = 10000003
        self.get(Links_242).values[9] = 10000004
        self.get(ChattingPlayer_356).values[9] = 10000001
        self.get(PoliceWin_362).values[9] = 9999998
        self.get(TerrorWin_363).values[9] = 9999998
        self.get(Shop1Blitter_372).values[9] = 9999999
        self.get(Shop2Blitter_373).values[9] = 9999999
        for item in self.get(C4_374, True):
            item.destroy()
        self.get(Shop1Blitter2_385).values[9] = 9999998
        self.get(Shop1Blitter3_386).values[9] = 9999998
        self.get(RealName_390).set_value(self.get(ClanTag_65).text+self.get(GlobalName_6).text)
        self.get(Fusssoldat_193).flags[21] = True
        self.get(Fusssoldat_193).flags[30] = False
        self.get(Head_441).destroy()
        self.get(Ini_55).set_item('Turning')
        self.values[13] = self.get(Ini_55).get_int()
        self.get(Chat_204).set_focus(False)
        self.set_event_id(4)
        if (self.get_global_value(1) == 1 and
        select(self.get(GlobalValues_165).values.get(0, 0) == 1)):
            self.get(Mapcycle_417).load('mapcycle.txt')
            self.get(ChosedMap_125).set_value(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(Mapcycle_417).get_line(2)+'.sdo')
            self.get(ChosedMapWithoutPath_126).set_value(self.get(Mapcycle_417).get_line(2))
            self.get(GlobalValues_165).values[1] = immediate_compare(to_number(self.get(Mapcycle_417).get_line(1)), '<', 1, 60, to_number(self.get(Mapcycle_417).get_line(1))*60)
            self.get(GlobalValues_165).values[2] = 2
            self.groups['Mapcycle active'] = True
        self.set_event_id(5)
        if self.players[1].lives == 1:
            self.groups['Footsteps'] = True
        self.set_event_id(6)
        if self.get_global_value(6) >= 2:
            self.get(PlShadow_382).destroy()
            self.get(PlShadow2_383).destroy()
        self.set_event_id(7)
        if self.get_global_value(6) == 1:
            self.groups['Graphic reduced'] = True
            self.get(PlShadow_382).set_effect('None')
            self.get(PlShadow2_383).set_effect('None')
        self.set_event_id(8)
        if self.get_global_value(6) == 2:
            self.groups['Graphic reduced 2'] = True
        self.set_event_id(9)
        if self.get_global_value(6) == 3:
            self.groups['Graphic reduced 3'] = True
        self.set_event_id(10)
        for item in self.get(Fusssoldat_193, True):
            if item.in_zone((-169, -193, 1089, 741)):
                item.flags[1] = False
        self.set_event_id(11)
        if self.get_global_value(9) == 0:
            self.get(Obj1WeaponList_314).set_direction(0)
            self.get(Obj1Weapon_308).force_animation('User defined 1')
        self.set_event_id(12)
        if self.get_global_value(9) == 1:
            self.get(Obj1WeaponList_314).set_direction(24)
            self.get(Obj1Weapon_308).force_animation('User defined 1')
        self.set_event_id(13)
        if self.get_global_value(1) == 1:
            self.get(Sting_186).set_value(make_random_key(10))
            self.get(Sting_186).set_value(filter_string(self.get(Sting_186).text))
            self.get(Moo_181).listen(to_number(self.get(Port_47).text))
            self.groups['Add server'] = True
            self.get(VisibleId_424).set_value(1)
            self.groups['Server main'] = True
            self.get(Moo2_447).listen(to_number(self.get(Port_47).text)+1)
        self.set_event_id(20)
        if self.get_global_value(2) == 0:
            self.get(Fusssoldat_193).values[5] = 100
            self.get(Fusssoldat_193).values[7] = 0
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 0
            self.get(Strafing_219).values[9] = 1000000
        self.set_event_id(21)
        self.get(StringParser_43).set_value(self.get(WeaponAllowed_59).text)
        self.get(Fusssoldat_193).values[8] = self.get_global_value(4)
        self.get(TurningSpeed_389).set_value(self.get_global_value(13))
        self.get(FastMouse_252).set_maximum(self.get(TurningSpeed_389).get_value()*2)
        add_encryption_key(self.get(Sting_186).text)
        self.set_event_id(22)
        if self.get(StringParser_43).get_element(-1 + 1) == '1':
            self.get(WeaponList_320).add_line('4')
            self.get(Fusssoldat_193).flags[4] = True
        self.set_event_id(23)
        if self.get(StringParser_43).get_element(-1 + 2) == '1':
            self.get(WeaponList_320).add_line('3')
            self.get(Fusssoldat_193).flags[3] = True
        self.set_event_id(24)
        if self.get(StringParser_43).get_element(-1 + 3) == '1':
            self.get(WeaponList_320).add_line('6')
            self.get(Fusssoldat_193).flags[6] = True
        self.set_event_id(25)
        if self.get(StringParser_43).get_element(-1 + 4) == '1':
            self.get(WeaponList_320).add_line('2')
            self.get(Fusssoldat_193).flags[2] = True
        self.set_event_id(26)
        if self.get(StringParser_43).get_element(-1 + 5) == '1':
            self.get(WeaponList_320).add_line('9')
            self.get(Fusssoldat_193).flags[9] = True
        self.set_event_id(27)
        if self.get(StringParser_43).get_element(-1 + 6) == '1':
            self.get(WeaponList_320).add_line('7')
            self.get(Fusssoldat_193).flags[7] = True
        self.set_event_id(28)
        if self.get(StringParser_43).get_element(-1 + 7) == '1':
            self.get(WeaponList_320).add_line('5')
            self.get(Fusssoldat_193).flags[5] = True
        self.set_event_id(29)
        if self.get(StringParser_43).get_element(-1 + 8) == '1':
            self.get(WeaponList_320).add_line('10')
            self.get(Fusssoldat_193).flags[10] = True
        self.set_event_id(30)
        if self.get(StringParser_43).get_element(-1 + 9) == '1':
            self.get(WeaponList_320).add_line('11')
            self.get(Fusssoldat_193).flags[11] = True
        self.set_event_id(31)
        if self.get(StringParser_43).get_element(-1 + 10) == '1':
            self.get(WeaponList_320).add_line('12')
            self.get(Fusssoldat_193).flags[12] = True
        self.set_event_id(32)
        if self.get_global_value(1) == 0:
            self.get(ChosedMap_125).set_value(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(ChosedMapWithoutPath_126).text)
            self.groups['Client main'] = True
            self.groups['Load Map'] = True
            self.groups['Client'] = True
            self.groups['Con'] = False
            self.get(Moo2_447).destroy()
            self.get(MooSock_335).destroy()
        self.set_event_id(36)
        os.remove('Screenshot.pak')
        self.set_event_id(37)
        self.capture_filename = 'screenshot'+str(self.get(ScreenshotNr_23).get_value())+'.bmp'
        open('Screenshot.pak', "wb").close()
        fp = open('Screenshot.pak', "ab")
        fp.write(str(self.get(ScreenshotNr_23).get_value()))
        fp.close()
        self.get(Fusssoldat_193).flags[30] = True
        self.set_event_id(1044)
        if self.groups['Custom Movement']:
            self.get(Active9_222).values[1] = 90
        pass
    
    def on_timer_1(self):
        self.set_event_id(33)
        if self.get(ChangeMap_217).text == self.get(MessageOfDay_58).text:
            self.get(ChangeMap_217).set_visible(False)
        pass
    
    def on_timer_2(self):
        self.set_event_id(541)
        if (self.groups['Game'] and self.get_global_value(12) == 1):
            self.groups['Music'] = True
        pass
    
    def loop_check_health(self):
        self.set_event_id(1028)
        if (self.groups['Server other Player'] and
        select(self.get(Fusssoldat2_194).values.get(21, 0) == self.get_loop_index('Check health')) and
        select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0)):
            return False # 'Check health'
        self.set_event_id(1029)
        if (self.groups['Server other Player'] and
        select(self.get(Fusssoldat2_194).values.get(21, 0) == self.get_loop_index('Check health')) and
        'self.get(Fusssoldat2_194).ObjectCount' == (self.get_loop_index('Check health')+1)):
            self.groups['Server other Player'] = False
            return False # 'Check health'
        pass

    def loop_b(self, klass, loop_index):
        x = self.get(BackgroundX_261).get_value()
        y = self.get(BackgroundY_262).get_value()
        back = self.create_object(klass, x, y)
        back.add_backdrop()
        back.destroy()
        if (loop_index+1)%7 != 0:
            self.get(BackgroundX_261).set_value(x+128)
        if (loop_index+1)%7 == 0:
            self.get(BackgroundY_262).set_value(y+128)
            self.get(BackgroundX_261).set_value(0)
    
    def loop_load(self, loop_index):
        self.set_event_id(384)
        if (self.groups['Load Map'] and
        loop_index == 0):
            encrypt_file(self.get(ChosedMap_125).text, 8)
            self.get(Follower_442).set_position(x = 399)
            self.get(Follower_442).set_position(y = 299)
        self.set_event_id(385)
        if (self.groups['Load Map'] and
        loop_index == 0 and
        self.get(CheckDaMap_176).text != self.get(Mapid_397).text and
        self.get_global_value(1) == 0):
            self.get(ErrorMsg_244).set_value('Map '+right_string(self.get(CheckKick_216).text, len(self.get(CheckKick_216).text)-5)+' differs from server')
            self.groups['Map change'] = False
            self.groups['Load Map'] = False
            self.groups['Disconnect'] = True
            return False
        self.set_event_id(386)
        if loop_index == 1:
            back_id = to_number(self.get(LoadMap_259).get_line(2))
            clear_color = None
            if back_id == 1:
                klass = Grass_256
                clear_color = (0, 255, 0)
            elif back_id == 2:
                klass = Desert_257
            elif back_id == 3:
                klass = Dust_258
            elif back_id == 4:
                klass = DarkGrass_422
                clear_color = (0, 255, 0)
            elif back_id == 5:
                klass = Water_423
                clear_color = (0, 0, 255)
            for loop_index in xrange(35):
                self.loop_b(klass, loop_index)
                if clear_color is not None:
                    self.get(OverlayRedux2_443).clear(*clear_color)
        self.set_event_id(411)
        if loop_index > 2 and loop_index + 1 < self.get(LoadMap_259).get_count():
            line = self.get(LoadMap_259).get_line(loop_index+1)
            object_id = to_number(line)
            self.get(StringParser_43).set_value(line)
            display_class = DISPLAY_IDS[object_id]
            x = to_number(self.get(StringParser_43).get_element(-1 + 2))
            y = to_number(self.get(StringParser_43).get_element(-1 + 3))
            display = self.create_object(display_class, x, y)
            if display_class in (SpawnArea_192, PoliceSpawn_345, 
                                 TerrorSpawn_346):
                display.set_visible(False)
            if display_class in (DeadTree_265, Tree3_278, Stone3_294,
                                 Pipeline_403, FenceHor_404, FenceVert_405):
                display.values[14] = 1

        self.set_event_id(471)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        self.get(LoadMap_259).get_count() != to_number(self.get(LoadMap_259).get_line(self.get(LoadMap_259).get_count())) and
        self.get_global_value(1) == 1):
            self.get(ExitCounter_221).set_value(4)
            self.get(ChangeMap_217).set_visible(True)
            self.get(ChangeMap_217).set_value('Closing server...')
            self.add_hud_line('Map file is invalid')
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('108')
            self.function_sendall()
            self.get(Edit2_336).set_value('GET http://www.seekanddread.de/Game/svr_del.php'+' HTTP/1.0'+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
            ResetGlobalTimer(0)
            self.get(MooSock_335).connect('www.seekanddread.de', 80)
            self.get(ServerError_60).set_value('Map file is invalid')
            self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+',,'+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
        self.set_event_id(472)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        self.get(LoadMap_259).get_count() != to_number(self.get(LoadMap_259).get_line(self.get(LoadMap_259).get_count())) and
        self.get_global_value(1) == 0):
            self.get(ErrorMsg_244).set_value('Map file is invalid')
            self.groups['Map change'] = False
            self.groups['Load Map'] = False
            self.groups['Disconnect'] = True
        self.set_event_id(473)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count()):
            for item in self.get(qualifier_1, True):
                item.values[9] = item.y * 1000 + item.x
            for i, item in enumerate(self.get(SpawnArea_192, True)):
                item.values[0] = i
        self.set_event_id(474)
        if (self.groups['Load Map'] and
        self.get_global_value(1) == 1 and
        loop_index+1 == self.get(LoadMap_259).get_count()):
            self.get(Edit2_336).set_value(self.get(ServerName_100).text+','+self.get(ChosedMapWithoutPath_126).text+','+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(HostIP_150).text+','+self.get(Port_47).text+','+self.get(Version_26).text+','+immediate_compare(self.get(SvrPw_155).text, '=', ' ', '0', '1'))
            self.get(BinaryObject_38).insert(self.get(Edit2_336).get_value(), 0)
            self.get(BinaryObject_38).BinaryEncodeBase64()
            self.get(BinaryObject_38).replace('+', '-')
            self.get(BinaryObject_38).replace('/', '_')
            self.get(BinaryObject_38).replace('=', '.')
            self.get(BinaryObject_38).replace('\n', '')
            self.get(BinaryObject_38).replace('\r', '')
            self.get(Edit2_336).set_value(self.get(BinaryObject_38).get_string(0, self.get(BinaryObject_38).get_size()))
            self.get(BinaryObject_38).clear()
            self.get(Edit2_336).set_value('GET http://www.seekanddread.de/Game/svr_add.php?sndserver='+self.get(Edit2_336).get_value()+' HTTP/1.0')
            self.get(Edit2_336).set_value(self.get(Edit2_336).get_value()+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
            self.get(MooSock_335).connect('www.seekanddread.de', 80)
            self.groups['Server'] = True
        self.set_event_id(475)
        if (self.groups['Load Map'] and
        self.get_global_value(1) == 1 and
        loop_index+1 == self.get(LoadMap_259).get_count()):
            self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+','+self.get(Version_26).text+','+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
        self.set_event_id(476)
        if (self.groups['Load Map'] and
        self.get_global_value(1) == 1 and
        loop_index+1 == self.get(LoadMap_259).get_count()):
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat_193).values[14] = 0
            self.get(RoundStart_361).set_value(0)
            self.get(Police2_357).set_value(0)
            self.get(Terror2_358).set_value(0)
            self.get(PoliceLeft_359).set_value(0)
            self.get(TerrorLeft_360).set_value(0)
        self.set_event_id(477)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count()):
            self.players[0].set_ignore(True)
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.get(Fusssoldat_193).values[12] = 0
            self.get(Fusssoldat_193).values[14] = 0
            self.get(Fusssoldat_193).values[7] = 0
            self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
            self.get(Strafing_219).movement.stop()
            self.get(Active6_214).set_visible(False)
            self.get(SkillCounter_211).set_value(0)
            self.get(Oben_239).set_visible(False)
            self.get(Unten_240).set_visible(False)
            self.get(Rechts_241).set_visible(False)
            self.get(Links_242).set_visible(False)
            self.get(Counter3_246).set_value(0)
            self.get(Snipercounter_438).set_value(0)
            self.groups['Weapon Change'] = True
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            for item in self.get(Strafing2_220, True):
                item.set_position(594, 693)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
        self.set_event_id(478)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count()):
            self.get(Killed_203).set_visible(False)
            self.get(Killed_203).set_value('')
            self.get(PoliceWin_362).set_position(-84, 671) # {'y': 671, 'x': -84}
            self.get(TerrorWin_363).set_position(-84, 671) # {'y': 671, 'x': -84}
            self.get(Cash_364).set_visible(False)
            self.get(_365).set_visible(False)
            self.get(Money_366).set_visible(False)
            self.get(Money_366).set_value(0)
            self.get(ScorePolice_368).set_visible(False)
            self.get(ScorePolice_368).set_value(0)
            self.get(ScoreTerror_369).set_visible(False)
            self.get(ScoreTerror_369).set_value(0)
            self.get(Score_367).set_visible(False)
            for item in self.get(WallDestroyed_376, True):
                item.destroy()
            for item in self.get(qualifier_6, True):
                item.restore_animation()
            for item in self.get(BoxDestroyed_377, True):
                item.destroy()
            for item in self.get(PipelineDestroyed_411, True):
                item.destroy()
            self.get(Fusssoldat_193).values[14] = 0
            for item in self.get(Fusssoldat2_194, True):
                item.values[25] = 0
            self.get(String31_437).set_value('0')
        self.set_event_id(479)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        len(self.get(SpawnArea_192, True)) > 0 and
        self.get(Modestatus_413).get_value() == 1):
            self.get(String2_200).set_visible(True)
            self.get(Respawn_201).set_visible(True)
            self.groups['Crates'] = True
        self.set_event_id(480)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        len(self.get(SpawnArea_192, True)) == 0 and
        len(self.get(PoliceSpawn_345, True)) >= 1 and
        len(self.get(TerrorSpawn_346, True)) >= 1 and
        self.get(Modestatus_413).get_value() == 1):
            self.get(Respawn_201).set_value(9)
            self.get(Cash_364).set_visible(True)
            self.get(_365).set_visible(True)
            self.get(Money_366).set_visible(True)
            self.get(ScorePolice_368).set_visible(True)
            self.get(ScoreTerror_369).set_visible(True)
            self.get(Score_367).set_visible(True)
            self.groups['Crates'] = False
            self.get(AmmoPack_208).destroy()
            self.get(Money_366).set_value(0)
            self.get(Respawn_201).set_visible(False)
            self.get(String2_200).set_visible(False)
            self.get(String31_437).set_value('0')
        self.set_event_id(481)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        select(self.get(Modestatus_413).get_value() == 2)):
            self.get(Respawn_201).set_value(9)
            self.get(Cash_364).set_visible(True)
            self.get(_365).set_visible(True)
            self.get(Money_366).set_visible(True)
            self.get(ScorePolice_368).set_visible(True)
            self.get(ScoreTerror_369).set_visible(True)
            self.get(Score_367).set_visible(True)
            self.groups['Crates'] = False
            for item in self.get(AmmoPack_208, True):
                item.destroy()
            self.get(Money_366).set_value(0)
            self.get(Respawn_201).set_visible(False)
            self.get(String2_200).set_visible(False)
            self.get(String31_437).set_value('0')
        self.set_event_id(482)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        select(self.get(Modestatus_413).get_value() == 3)):
            self.get(Respawn_201).set_value(9)
            self.get(ScorePolice_368).set_visible(True)
            self.get(ScoreTerror_369).set_visible(True)
            self.get(Score_367).set_visible(True)
            self.get(Respawn_201).set_visible(False)
            self.get(String2_200).set_visible(False)
            self.groups['Crates'] = True
        self.set_event_id(483)
        if (self.groups['Load Map'] and
        self.get_global_value(1) == 0 and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        select(negate(self.get(Moo_181).is_connected())) and
        select(len(self.get(SpawnArea_192, True)) == 0) and
        select(len(self.get(PoliceSpawn_345, True)) >= 1) and
        select(len(self.get(TerrorSpawn_346, True)) >= 1) and
        select(self.get(Modestatus_413).get_value() == 1)):
            self.get(Mode_344).set_value(1)
            self.get(DM_412).set_value(0)
        self.set_event_id(484)
        if (self.groups['Load Map'] and
        self.get_global_value(1) == 0 and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        select(negate(self.get(Moo_181).is_connected())) and
        select(self.get(Modestatus_413).get_value() == 2)):
            self.get(Mode_344).set_value(1)
            self.get(DM_412).set_value(0)
        self.set_event_id(485)
        if (self.groups['Load Map'] and
        self.get_global_value(1) == 0 and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        select(negate(self.get(Moo_181).is_connected())) and
        select(self.get(Modestatus_413).get_value() == 3)):
            self.get(Mode_344).set_value(1)
        self.set_event_id(486)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count()):
            self.groups['Background'] = True
            self.groups['Load Map'] = False
            self.do_sort()
        self.set_event_id(487)
        if (self.groups['Load Map'] and
        loop_index+1 == self.get(LoadMap_259).get_count() and
        self.pick_objects(zone = (-169, -193, 1089, 741))):
            self.get(Fusssoldat_193).flags[1] = True
            self.get(Fusssoldat_193).flags[1] = False
        pass

    def do_sort(self):
        # SortByAlterableDecreasing(9, 10000000)
        self.instances.sort(key = lambda x: x.values.get(9, 10000000))
    
    def loop_spawn(self, loop_index):
        self.set_event_id(625)
        if (loop_index == 0 and self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[21] == True)):
            self.get(Fusssoldat_193).flags[21] = False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('219'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[8]))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(626)
        if (select(self.groups['Game'] and self.get(SpawnArea_192).PickRandom()) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Fusssoldat2_194))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(627)
        if (self.groups['Game'] and
        select(self.get(SpawnArea_192).PickRandom()) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Gaswolke_215))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(628)
        if (self.groups['Game'] and
        select(self.get(SpawnArea_192).PickRandom()) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Exp_247))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(629)
        if (self.groups['Game'] and
        select(self.get(SpawnArea_192).PickRandom()) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Exp_247))) and
        select(negate(self.get(SpawnArea_192).IsOverlapping(Gaswolke_215))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(630)
        if (self.groups['Game'] and
        loop_index == 99 and
        select(self.get(SpawnArea_192).PickRandom())):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(SpawnArea_192).x + 0, self.get(SpawnArea_192).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(SpawnArea_192)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        pass
    
    def loop_flash(self, loop_index):
        self.set_event_id(567)
        if (self.groups['Game'] and
        loop_index == 0 and
        select(self.get(Flash_380).CompareX(self.get(Fusssoldat_193).x)) and
        select(self.get(Flash_380).CompareY(self.get(Fusssoldat_193).y))):
            self.get(FlashTime_381).set_value(self.get(Flash_380).values[1])
            self.get(Flash_380).destroy()
            self.get(Accuracy_238).set_value(50)
            self.groups['Flashed'] = True
            return False
        self.set_event_id(568)
        if (self.groups['Game'] and
        loop_index == 0 and
        abs(self.get(Flash_380).values[23]) >= abs(self.get(Flash_380).values[24])):
            self.get(Flash_380).values[12] = (self.get(Fusssoldat_193).y*1.0-self.get(Flash_380).y*1.0)/(self.get(Fusssoldat_193).x*1.0-self.get(Flash_380).x*1.0)
            self.get(Flash_380).values[13] = self.get(Flash_380).y*1.0-(self.get(Flash_380).values[12]*1.0*self.get(Flash_380).x*1.0)
        self.set_event_id(569)
        if (self.groups['Game'] and
        loop_index == 0 and
        abs(self.get(Flash_380).values[23]) < abs(self.get(Flash_380).values[24])):
            self.get(Flash_380).values[12] = (self.get(Fusssoldat_193).x*1.0-self.get(Flash_380).x*1.0)/(self.get(Fusssoldat_193).y*1.0-self.get(Flash_380).y*1.0)
            self.get(Flash_380).values[13] = self.get(Flash_380).x*1.0-(self.get(Flash_380).values[12]*1.0*self.get(Flash_380).y*1.0)
        self.set_event_id(570)
        if (self.groups['Game'] and
        abs(self.get(Flash_380).values[23]) >= abs(self.get(Flash_380).values[24])):
            self.get(Flash_380).set_position(x = self.get(Flash_380).x+self.get(Flash_380).values[21])
            self.get(Flash_380).set_position(y = self.get(Flash_380).values[12]*1.0*self.get(Flash_380).x*1.0+self.get(Flash_380).values[13]*1.0)
        self.set_event_id(571)
        if (self.groups['Game'] and
        abs(self.get(Flash_380).values[23]) < abs(self.get(Flash_380).values[24])):
            self.get(Flash_380).set_position(y = self.get(Flash_380).y+self.get(Flash_380).values[22])
            self.get(Flash_380).set_position(x = self.get(Flash_380).values[12]*1.0*self.get(Flash_380).y*1.0+self.get(Flash_380).values[13]*1.0)
        self.set_event_id(572)
        if (self.groups['Game'] and
        select(self.get(Flash_380).OnCollision(Strafing_219)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
            self.get(FlashTime_381).set_value(self.get(Flash_380).values[1])
            self.get(Flash_380).destroy()
            self.get(Accuracy_238).set_value(50)
            self.groups['Flashed'] = True
            return False
        self.set_event_id(573)
        if (self.groups['Game'] and
        select(self.get(Flash_380).OnCollision(Strafing_219)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0)):
            self.get(Flash_380).destroy()
            return False
        self.set_event_id(574)
        if self.groups['Game']:
            self.get(Flash_380).values[9] = self.get(Flash_380).y*1000
            self.get(Flash_380).values[1] -= 2
        self.set_event_id(575)
        if (self.groups['Game'] and
        select(self.get(Flash_380).OnCollision(qualifier_6))):
            self.get(Flash_380).destroy()
            return False
        self.set_event_id(576)
        if (self.groups['Game'] and
        select(self.get(Flash_380).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Flash_380).values[9]) and
        select(self.get(Flash_380).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.get(Flash_380).destroy()
            return False
        self.set_event_id(577)
        if (self.groups['Game'] and
        select(self.get(Flash_380).OutsidePlayfield())):
            self.get(Flash_380).destroy()
            return False
        self.set_event_id(578)
        if (self.groups['Game'] and
        max(abs(self.get(Flash_380).values[23]), abs(self.get(Flash_380).values[24])) == loop_index and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
            self.get(FlashTime_381).set_value(self.get(Flash_380).values[1])
            self.get(Flash_380).destroy()
            self.get(Accuracy_238).set_value(50)
            self.groups['Flashed'] = True
            return False
        self.set_event_id(579)
        if (self.groups['Game'] and
        max(abs(self.get(Flash_380).values[23]), abs(self.get(Flash_380).values[24])) == loop_index):
            self.get(Flash_380).destroy()
            return False
        pass
    
    def loop_waffe12(self, loop_index):
        self.set_event_id(1361)
        if (self.groups['W 12'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((12+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1362)
        if (self.groups['W 12'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((12+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1363)
        if (self.groups['W 12'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1364)
        if (self.groups['W 12'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((12+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1365)
        if (self.groups['W 12'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((12+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1366)
        if (self.groups['W 12'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+12))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1367)
        if (self.groups['W 12'] and
        loop_index == 799):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((12+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1368)
        if (self.groups['W 12'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1200000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1369)
        if (self.groups['W 12'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1370)
        if (self.groups['W 12'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1200000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
            return False
        self.set_event_id(1371)
        if (self.groups['W 12'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1372)
        if self.groups['W 12']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1373)
        if (self.groups['W 12'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_kick_timeout(self, loop_index):
        self.set_event_id(170)
        if self.groups['Server main']:
            self.get(Moo_181).SelectSocket(loop_index+1)
        self.set_event_id(171)
        if (self.groups['Server main'] and
        to_number(self.get(Timeout1_448).get_line(loop_index+1)) >= 4):
            self.get(Moo_181).delete_socket()
        pass
    
    def loop_team_count(self, loop_index):
        self.set_event_id(972)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(DM_412).get_value() == 1)):
            return False
        self.set_event_id(973)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(InvincibleTime_388).get_value() > 0)):
            return False
        self.set_event_id(974)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(PoliceWin_362).InsidePlayfield())):
            return False
        self.set_event_id(975)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(TerrorWin_363).InsidePlayfield())):
            return False
        self.set_event_id(976)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(ExitCounter_221).get_value() > 0)):
            return False
        self.set_event_id(977)
        if (self.groups['Server'] and
        loop_index == 0):
            self.get(PoliceLeft_359).set_value(0)
            self.get(TerrorLeft_360).set_value(0)
            self.get(Police2_357).set_value(0)
            self.get(Terror2_358).set_value(0)
            self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
        self.set_event_id(978)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1)):
            self.get(Police2_357).add_value(1)
        self.set_event_id(979)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
            self.get(PoliceLeft_359).add_value(1)
        self.set_event_id(980)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2)):
            self.get(Terror2_358).add_value(1)
        self.set_event_id(981)
        if (self.groups['Server'] and
        loop_index == 0 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
            self.get(TerrorLeft_360).add_value(1)
        self.set_event_id(982)
        if (self.groups['Server'] and
        self.get(Fusssoldat2_194).values[21] == loop_index and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 1)):
            self.get(Police2_357).add_value(1)
        self.set_event_id(983)
        if (self.groups['Server'] and
        self.get(Fusssoldat2_194).values[21] == loop_index and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(PoliceLeft_359).add_value(1)
        self.set_event_id(984)
        if (self.groups['Server'] and
        self.get(Fusssoldat2_194).values[21] == loop_index and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 2)):
            self.get(Terror2_358).add_value(1)
        self.set_event_id(985)
        if (self.groups['Server'] and
        self.get(Fusssoldat2_194).values[21] == loop_index and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 2) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(TerrorLeft_360).add_value(1)
        self.set_event_id(986)
        if (self.groups['Server'] and
        self.get(Players_317).get_value() == loop_index+1 and
        select(self.get(PoliceLeft_359).get_value() == 0) and
        select(self.get(TerrorLeft_360).get_value() == 0) and
        select(self.get(DM_412).get_value() == 0)):
            self.get(RoundStart_361).set_value(7)
            self.get(InvincibleTime_388).set_value(12)
            return False
        self.set_event_id(987)
        if (self.groups['Server'] and
        self.get(Players_317).get_value() == loop_index+1 and
        select(self.get(PoliceLeft_359).get_value() == 0) and
        select(self.get(TerrorLeft_360).get_value() > 0) and
        select(self.get(Police2_357).get_value() > 0) and
        select(self.get(Terror2_358).get_value() > 0) and
        select(self.get(RoundStart_361).get_value() == 0) and
        select(self.get(DM_412).get_value() == 0)):
            PlaySample(start1_22)
            self.get(TerrorWin_363).set_position(400, 300) # {'y': 300, 'x': 400}
            self.get(ScoreTerror_369).add_value(1)
            self.get(RoundStart_361).set_value(7)
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(InvincibleTime_388).set_value(12)
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('215'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror')
            self.function_sendall()
            self.function_csmup()
            self.get(Counter3_246).set_value(0)
            self.get(Snipercounter_438).set_value(0)
            return False
        self.set_event_id(988)
        if (self.groups['Server'] and
        self.get(Players_317).get_value() == loop_index+1 and
        select(self.get(TerrorLeft_360).get_value() == 0) and
        select(self.get(PoliceLeft_359).get_value() > 0) and
        select(self.get(Police2_357).get_value() > 0) and
        select(self.get(Terror2_358).get_value() > 0) and
        select(self.get(RoundStart_361).get_value() == 0) and
        select(self.get(DM_412).get_value() == 0)):
            PlaySample(start1_22)
            self.get(RoundStart_361).set_value(7)
            self.get(ScorePolice_368).add_value(1)
            self.get(PoliceWin_362).set_position(400, 300) # {'y': 300, 'x': 400}
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(InvincibleTime_388).set_value(12)
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('215'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police')
            self.function_sendall()
            self.function_csmup()
            self.get(Counter3_246).set_value(0)
            self.get(Snipercounter_438).set_value(0)
            return False
        pass
    
    def loop_check_timeout(self, loop_index):
        self.set_event_id(168)
        if self.groups['Server main']:
            self.get(Moo_181).SelectSocket(loop_index+1)
            self.get(Timeout1_448).add_line(self.get(Moo_181).get_property('timeout'))
        pass
    
    def loop_c4s(self, loop_index):
        self.set_event_id(111)
        if (self.groups['Server main'] and
        select(self.get(C4_374).values.get(21, 0) == loop_index)):
            self.get(Msg_427).set_value('212'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(C4_374).values[2]), str(self.get(C4_374).values[2]))+str(((self.get(C4_374).values[4]+64)+self.get(C4_374).x*100+self.get(C4_374).y*100000))+str(self.get(Csm_432).get_value()))
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        pass
    
    def loop_timeout2(self, loop_index):
        self.set_event_id(166)
        if self.groups['Server main']:
            self.get(Moo2_447).SelectSocket(loop_index+1)
            self.get(Moo2_447).set_property('timeout', str(to_number(self.get(Moo2_447).get_property('timeout'))+1))
        pass
    
    def loop_send(self, loop_index):
        self.set_event_id(66)
        if self.groups['Server main']:
            self.get(Moo_181).SelectSocket(loop_index+1)
            self.get(Sall_446).set_value(self.get(Moo_181).get_property('snd'))
        self.set_event_id(67)
        if (self.groups['Server main'] and
        to_number(self.get(Sall_446).text) != self.get(NotID_430).get_value() and
        self.get(Sall_446).text != '0' and
        self.get(Sall_446).text != ''):
            self.get(Moo_181).send_line(self.get(Temp_431).text)
        pass
    
    def loop_crates(self, loop_index):
        self.set_event_id(108)
        if (self.groups['Server main'] and
        select(self.get(AmmoPack_208).values.get(21, 0) == loop_index)):
            self.get(Msg_427).set_value('20701'+str((self.get(AmmoPack_208).x+self.get(AmmoPack_208).y*1000+'self.get(AmmoPack_208).GetDirection'*1000000))+immediate_compare(self.get(AmmoPack_208).values[0], '<', 10, '0'+str(self.get(AmmoPack_208).values[0]), str(self.get(AmmoPack_208).values[0]))+str(self.get(Csm_432).get_value()))
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        pass
    
    def loop_drawback(self, loop_index):
        self.set_event_id(504)
        if (self.groups['Background'] and
        select(self.get(GroundBackground_266).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(GroundBackground_266).x-96, self.get(GroundBackground_266).y-98, 192, 196, 0, 0, 0)
        self.set_event_id(505)
        if (self.groups['Background'] and
        select(self.get(Dust2_416).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Dust2_416).x, self.get(Dust2_416).y, 128, 128, 0, 0, 0)
        self.set_event_id(506)
        if (self.groups['Background'] and
        select(self.get(Desert2_415).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Desert2_415).x, self.get(Desert2_415).y, 128, 128, 0, 0, 0)
        self.set_event_id(507)
        if (self.groups['Background'] and
        select(self.get(Grass2_414).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Grass2_414).x, self.get(Grass2_414).y, 64, 64, 0, 255, 0)
        self.set_event_id(508)
        if (self.groups['Background'] and
        select(self.get(Street_274).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Street_274).x-32, self.get(Street_274).y-42, 64, 88, 192, 192, 192)
        self.set_event_id(509)
        if (self.groups['Background'] and
        select(self.get(Street2_279).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Street2_279).x-48, self.get(Street2_279).y-34, 88, 64, 192, 192, 192)
        self.set_event_id(510)
        if (self.groups['Background'] and
        select(self.get(Crossroad_281).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Crossroad_281).x-48, self.get(Crossroad_281).y-34, 88, 88, 192, 192, 192)
        self.set_event_id(511)
        if (self.groups['Background'] and
        select(self.get(Sidewalk_272).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Sidewalk_272).x-32, self.get(Sidewalk_272).y-2, 64, 16, 192, 192, 192)
        self.set_event_id(512)
        if (self.groups['Background'] and
        select(self.get(BrokenSidewalk_273).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(BrokenSidewalk_273).x-32, self.get(BrokenSidewalk_273).y-2, 64, 16, 192, 192, 192)
        self.set_event_id(513)
        if (self.groups['Background'] and
        select(self.get(Sidewalk2_280).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Sidewalk2_280).x-8, self.get(Sidewalk2_280).y-34, 16, 64, 192, 192, 192)
        self.set_event_id(514)
        if (self.groups['Background'] and
        select(self.get(Floor_296).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Floor_296).x-16, self.get(Floor_296).y-16, 32, 32, 192, 192, 192)
        self.set_event_id(515)
        if (self.groups['Background'] and
        select(self.get(Floor2_297).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(Floor2_297).x-16, self.get(Floor2_297).y-16, 32, 32, 192, 192, 192)
        self.set_event_id(516)
        if (self.groups['Background'] and
        select(self.get(WoodenFloor_298).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(WoodenFloor_298).x-32, self.get(WoodenFloor_298).y-32, 64, 64, 128, 128, 0)
        self.set_event_id(517)
        if (self.groups['Background'] and
        select(self.get(StoneFloor_299).values.get(11, 0) == loop_index)):
            self.get(OverlayRedux2_443).OverlayDrawRectangle(self.get(StoneFloor_299).x-32, self.get(StoneFloor_299).y-32, 64, 64, 192, 192, 192)
        pass
    
    def loop_checkid(self, loop_index):
        self.set_event_id(117)
        if (self.groups['Server main'] and
        self.get(Fusssoldat2_194).values[21] == loop_index and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == self.get(IdAllocation_425).get_value())):
            self.get(IdAllocation_425).add_value(1)
            return False
        self.set_event_id(118)
        if (self.groups['Server main'] and
        loop_index+1 == self.get(Players_317).get_value()):
            return False
        pass
    
    def loop_spawn_t(self, loop_index):
        self.set_event_id(637)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 0)):
            return False
        self.set_event_id(638)
        if (self.groups['Game'] and
        select(self.get(TerrorSpawn_346).PickRandom()) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Fusssoldat2_194))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(639)
        if (self.groups['Game'] and
        select(self.get(TerrorSpawn_346).PickRandom()) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Gaswolke_215))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(640)
        if (self.groups['Game'] and
        select(self.get(TerrorSpawn_346).PickRandom()) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Exp_247))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(641)
        if (self.groups['Game'] and
        select(self.get(TerrorSpawn_346).PickRandom()) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Exp_247))) and
        select(negate(self.get(TerrorSpawn_346).IsOverlapping(Gaswolke_215))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(642)
        if (self.groups['Game'] and
        loop_index == 99 and
        select(self.get(TerrorSpawn_346).PickRandom())):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        pass
    
    def loop_check_timeout2(self, loop_index):
        self.set_event_id(169)
        if self.groups['Server main']:
            self.get(Moo2_447).SelectSocket(loop_index+1)
            self.get(Timeout1_448).add_line(self.get(Moo2_447).get_property('timeout'))
        pass
    
    def loop_waffe7(self, loop_index):
        self.set_event_id(1271)
        if (self.groups['W 7'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((7+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1272)
        if (self.groups['W 7'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((7+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1273)
        if (self.groups['W 7'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1274)
        if (self.groups['W 7'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((7+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1275)
        if (self.groups['W 7'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((7+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1276)
        if (self.groups['W 7'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+7))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1277)
        if (self.groups['W 7'] and
        loop_index >= 499):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((7+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1278)
        if (self.groups['W 7'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+700000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            return False
        self.set_event_id(1279)
        if (self.groups['W 7'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1280)
        if (self.groups['W 7'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+700000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
            return False
        self.set_event_id(1281)
        if (self.groups['W 7'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1282)
        if self.groups['W 7']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1283)
        if (self.groups['W 7'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_spawn_p(self, loop_index):
        self.set_event_id(631)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 0)):
            return False
        self.set_event_id(632)
        if (self.groups['Game'] and
        select(self.get(PoliceSpawn_345).PickRandom()) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Fusssoldat2_194))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(633)
        if (self.groups['Game'] and
        select(self.get(PoliceSpawn_345).PickRandom()) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Gaswolke_215))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(634)
        if (self.groups['Game'] and
        select(self.get(PoliceSpawn_345).PickRandom()) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Exp_247))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(635)
        if (self.groups['Game'] and
        select(self.get(PoliceSpawn_345).PickRandom()) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Fusssoldat2_194))) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Exp_247))) and
        select(negate(self.get(PoliceSpawn_345).IsOverlapping(Gaswolke_215))) and
        select(self.get(Gaswolke_215).NumberOfObjects(0)) and
        select(self.get(Exp_247).NumberOfObjects(0))):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(636)
        if (loop_index == 99 and
        select(self.get(PoliceSpawn_345).PickRandom())):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(String2_200).set_visible(False)
            self.get(Respawn_201).set_visible(False)
            self.get(Respawn_201).set_value(5)
            self.get(Strafing_219).set_position(self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)'}
            self.get(Fusssoldat_193).set_visible(True)
            RestoreControls()
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Fusssoldat_193).values[7] = 1
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.get(SkillCounter_211).set_value(0)
            self.get(Fusssoldat_193).values[15] = 0
            self.create_object(MagicExplode3_212, self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)', 'create_object': 'MagicExplode3_212'}
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(Active9_222).values[7] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        pass
    
    def loop_waffe9(self, loop_index):
        self.set_event_id(1307)
        if (self.groups['W 9'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((9+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1308)
        if (self.groups['W 9'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((9+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1309)
        if (self.groups['W 9'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1310)
        if (self.groups['W 9'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((9+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1311)
        if (self.groups['W 9'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((9+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1312)
        if (self.groups['W 9'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+9))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1313)
        if (self.groups['W 9'] and
        loop_index == 499):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((9+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1314)
        if (self.groups['W 9'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+900000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            return False
        self.set_event_id(1315)
        if (self.groups['W 9'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1316)
        if (self.groups['W 9'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+900000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
            return False
        self.set_event_id(1317)
        if (self.groups['W 9'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1318)
        self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
        self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
        self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1319)
        if (self.groups['W 9'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_sort(self, loop_index):
        self.set_event_id(715)
        if (to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-loop_index)) < to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1)))):
            return False
        self.set_event_id(716)
        if (to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-loop_index)) == to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1)))):
            self.get(StringParser_43).set_value(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1)))
            self.get(ScoreBar_234).values[1] = to_number(self.get(StringParser_43).get_element(-1 + 5))
        self.set_event_id(717)
        if (to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-loop_index)) == to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1))) and
        select(self.get(ScoreBar_234).values.get(0, 0) < self.get(ScoreBar_234).values[1])):
            self.get(ScoreBoard_231).ListInsertLine('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1), self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index)))
            self.get(ScoreBoard_231).delete_line('self.get(ScoreBoard_231).ListGetLineCount'-loop_index)
        self.set_event_id(718)
        if (to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-loop_index)) == to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1))) and
        select(self.get(ScoreBar_234).values.get(0, 0) >= self.get(ScoreBar_234).values[1])):
            return False
        self.set_event_id(719)
        if (to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-loop_index)) > to_number(self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1)))):
            self.get(ScoreBoard_231).ListInsertLine('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index+1), self.get(ScoreBoard_231).get_line('self.get(ScoreBoard_231).ListGetLineCount'-(loop_index)))
            self.get(ScoreBoard_231).delete_line('self.get(ScoreBoard_231).ListGetLineCount'-loop_index)
        pass
    
    def loop_pinfo(self, loop_index):
        self.set_event_id(96)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(21, 0) == loop_index) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) != to_number(self.get(Moo_181).get_property('sndnew'))) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
            self.get(Msg_427).set_value('105'+immediate_compare(self.get(Fusssoldat2_194).values[12], '<', 10, ('0'+str(self.get(Fusssoldat2_194).values[12])), str(self.get(Fusssoldat2_194).values[12])))
            self.get(Msg_427).set_value(self.get(Msg_427).text+str('self.get(Strafing2_220).GetDirection')+','+str('self.get(Strafing2_220).Speed')+','+str(self.get(Strafing2_220).x)+','+str(self.get(Strafing2_220).y)+','+str(self.get(Fusssoldat2_194).values[25])+','+str(self.get(Fusssoldat2_194).values[17])+','+str(self.get(Fusssoldat2_194).values[8])+','+str(self.get(Fusssoldat2_194).values[18])+','+str(self.get(Chatting_355).values[1])+','+str(self.get(Fusssoldat2_194).values[7])+','+self.get(NameTag2_429).get_text())
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        pass
    
    def loop_doubleip(self, loop_index):
        self.set_event_id(43)
        self.get(Moo_181).select_socket(loop_index+1)
        self.set_event_id(44)
        if (self.groups['Con'] and
        self.get(Msg_427).text == 'self.get(Moo_181).SockGetRemoteIP'):
            self.get(Moo_181).select_socket('self.get(Moo_181).SockCountSockets'-1)
            self.get(Moo_181).delete_socket()
            return False
        pass
    
    def loop_waffe10(self, loop_index):
        self.set_event_id(1325)
        if (self.groups['W 10'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((10+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1326)
        if (self.groups['W 10'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((10+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1327)
        if (self.groups['W 10'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1328)
        if (self.groups['W 10'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((10+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1329)
        if (self.groups['W 10'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((10+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1330)
        if (self.groups['W 10'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+10))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1331)
        if (self.groups['W 10'] and
        loop_index == 449):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((10+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1332)
        if (self.groups['W 10'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            return False
        self.set_event_id(1333)
        if (self.groups['W 10'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1334)
        if (self.groups['W 10'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1000000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
            return False
        self.set_event_id(1335)
        if (self.groups['W 10'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1336)
        self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
        self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
        self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1337)
        if (self.groups['W 10'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_entry(self, loop_index):
        self.set_event_id(720)
        if (select(self.get(Fusssoldat2_194).values.get(21, 0) == loop_index) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
            self.get(ScoreBoard_231).add_line(str(self.get(Fusssoldat2_194).values[7])+','+self.get(NameTag2_429).get_text()+','+str(self.get(Fusssoldat2_194).values[12])+','+str(self.get(Fusssoldat2_194).values[17])+','+str(self.get(Fusssoldat2_194).values[8])+',0,'+str(self.get(Fusssoldat2_194).values[18]))
            self.get(ScoreBar_234).values[0] = self.get(Fusssoldat2_194).values[8]
            for loop_index in xrange('self.get(ScoreBoard_231).ListGetLineCount'-1):
                if self.loop_sort(loop_index) == False: break
        pass
    
    def loop_waffe11(self, loop_index):
        self.set_event_id(1343)
        if (self.groups['W 11'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((11+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1344)
        if (self.groups['W 11'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((11+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1345)
        if (self.groups['W 11'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1346)
        if (self.groups['W 11'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((11+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1347)
        if (self.groups['W 11'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((11+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1348)
        if (self.groups['W 11'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+11))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1349)
        if (self.groups['W 11'] and
        loop_index == 799):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((11+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1350)
        if (self.groups['W 11'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1351)
        if (self.groups['W 11'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1352)
        if (self.groups['W 11'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(1353)
        if (self.groups['W 11'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1354)
        if self.groups['W 11']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1355)
        if (self.groups['W 11'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_userishere(self, loop_index):
        self.set_event_id(100)
        if (self.groups['Server main'] and
        select(self.get(NameTag2_429).values.get(21, 0) == loop_index) and
        False):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '102'+immediate_compare(self.get(NameTag2_429).values[0], '<', 10, '0'+str(self.get(NameTag2_429).values[0]), str(self.get(NameTag2_429).values[0]))+self.get(NameTag2_429).get_text()))
        pass
    
    def loop_alloid(self, loop_index):
        self.set_event_id(115)
        if (self.groups['Server main'] and
        select(self.get(Players_317).get_value() == 1)):
            return False
        self.set_event_id(116)
        if (self.groups['Server main'] and
        select(self.get(Players_317).get_value() > 1)):
            for loop_index in xrange(self.get(Players_317).get_value()-1):
                if self.loop_checkid(loop_index) == False: break
        pass
    
    def loop_list(self, loop_index):
        self.set_event_id(721)
        if self.groups['Game']:
            self.get(StringParser_43).set_value(self.get(ScoreBoard_231).get_line(loop_index+1))
        self.set_event_id(722)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) != '1' and
        select(self.get(Mode_344).get_value() == 0)):
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
        self.set_event_id(723)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) == '1' and
        select(self.get(Mode_344).get_value() == 0)):
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
            self.get(Player_334).set_position(x = 229)
            self.get(Player_334).set_position(y = 158+loop_index*16)
        self.set_event_id(724)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) != '1' and
        self.get(StringParser_43).get_element(-1 + 7) == '0' and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(NameScore3_351).set_value(self.get(NameScore3_351).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore3_352).set_value(self.get(FragsScore3_352).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore3_353).set_value(self.get(IdScore3_353).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing3_354).set_value(self.get(IdPing3_354).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+'\r\n')
            self.get(NameScore2_347).set_value(self.get(NameScore2_347).text+'\r\n')
            self.get(FragsScore2_348).set_value(self.get(FragsScore2_348).text+'\r\n')
            self.get(IdScore2_349).set_value(self.get(IdScore2_349).text+'\r\n')
            self.get(IdPing2_350).set_value(self.get(IdPing2_350).text+'\r\n')
        self.set_event_id(725)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) == '1' and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 0) and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(Player_334).set_position(x = 229)
            self.get(Player_334).set_position(y = 158+loop_index*16)
            self.get(NameScore3_351).set_value(self.get(NameScore3_351).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore3_352).set_value(self.get(FragsScore3_352).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore3_353).set_value(self.get(IdScore3_353).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing3_354).set_value(self.get(IdPing3_354).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+'\r\n')
            self.get(NameScore2_347).set_value(self.get(NameScore2_347).text+'\r\n')
            self.get(FragsScore2_348).set_value(self.get(FragsScore2_348).text+'\r\n')
            self.get(IdScore2_349).set_value(self.get(IdScore2_349).text+'\r\n')
            self.get(IdPing2_350).set_value(self.get(IdPing2_350).text+'\r\n')
        self.set_event_id(726)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) != '1' and
        self.get(StringParser_43).get_element(-1 + 7) == '1' and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(NameScore2_347).set_value(self.get(NameScore2_347).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore2_348).set_value(self.get(FragsScore2_348).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore2_349).set_value(self.get(IdScore2_349).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing2_350).set_value(self.get(IdPing2_350).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+'\r\n')
            self.get(NameScore3_351).set_value(self.get(NameScore3_351).text+'\r\n')
            self.get(FragsScore3_352).set_value(self.get(FragsScore3_352).text+'\r\n')
            self.get(IdScore3_353).set_value(self.get(IdScore3_353).text+'\r\n')
            self.get(IdPing3_354).set_value(self.get(IdPing3_354).text+'\r\n')
        self.set_event_id(727)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) == '1' and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(Player_334).set_position(x = 229)
            self.get(Player_334).set_position(y = 158+loop_index*16)
            self.get(NameScore2_347).set_value(self.get(NameScore2_347).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore2_348).set_value(self.get(FragsScore2_348).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore2_349).set_value(self.get(IdScore2_349).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing2_350).set_value(self.get(IdPing2_350).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+'\r\n')
            self.get(NameScore3_351).set_value(self.get(NameScore3_351).text+'\r\n')
            self.get(FragsScore3_352).set_value(self.get(FragsScore3_352).text+'\r\n')
            self.get(IdScore3_353).set_value(self.get(IdScore3_353).text+'\r\n')
            self.get(IdPing3_354).set_value(self.get(IdPing3_354).text+'\r\n')
        self.set_event_id(728)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) != '1' and
        self.get(StringParser_43).get_element(-1 + 7) == '2' and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
            self.get(NameScore2_347).set_value(self.get(NameScore2_347).text+'\r\n')
            self.get(FragsScore2_348).set_value(self.get(FragsScore2_348).text+'\r\n')
            self.get(IdScore2_349).set_value(self.get(IdScore2_349).text+'\r\n')
            self.get(IdPing2_350).set_value(self.get(IdPing2_350).text+'\r\n')
            self.get(NameScore3_351).set_value(self.get(NameScore3_351).text+'\r\n')
            self.get(FragsScore3_352).set_value(self.get(FragsScore3_352).text+'\r\n')
            self.get(IdScore3_353).set_value(self.get(IdScore3_353).text+'\r\n')
            self.get(IdPing3_354).set_value(self.get(IdPing3_354).text+'\r\n')
        self.set_event_id(729)
        if (self.groups['Game'] and
        self.get(StringParser_43).get_element(-1 + 6) == '1' and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(Player_334).set_position(x = 229)
            self.get(Player_334).set_position(y = 158+loop_index*16)
            self.get(NameScore_235).set_value(self.get(NameScore_235).text+self.get(StringParser_43).get_element(-1 + 2)+'\r\n')
            self.get(FragsScore_236).set_value(self.get(FragsScore_236).text+self.get(StringParser_43).get_element(-1 + 1)+' / '+self.get(StringParser_43).get_element(-1 + 5)+'\r\n')
            self.get(IdScore_237).set_value(self.get(IdScore_237).text+self.get(StringParser_43).get_element(-1 + 3)+'\r\n')
            self.get(IdPing_307).set_value(self.get(IdPing_307).text+self.get(StringParser_43).get_element(-1 + 4)+'\r\n')
            self.get(NameScore2_347).set_value(self.get(NameScore2_347).text+'\r\n')
            self.get(FragsScore2_348).set_value(self.get(FragsScore2_348).text+'\r\n')
            self.get(IdScore2_349).set_value(self.get(IdScore2_349).text+'\r\n')
            self.get(IdPing2_350).set_value(self.get(IdPing2_350).text+'\r\n')
            self.get(NameScore3_351).set_value(self.get(NameScore3_351).text+'\r\n')
            self.get(FragsScore3_352).set_value(self.get(FragsScore3_352).text+'\r\n')
            self.get(IdScore3_353).set_value(self.get(IdScore3_353).text+'\r\n')
            self.get(IdPing3_354).set_value(self.get(IdPing3_354).text+'\r\n')
        self.set_event_id(730)
        if (self.groups['Game'] and
        loop_index+1 == 'self.get(ScoreBoard_231).ListGetLineCount'):
            self.get(ErrorMsg_244).set_value('*'+self.get(ErrorMsg_244).text)
        pass
    
    def loop_waffe8(self, loop_index):
        self.set_event_id(1289)
        if (self.groups['W 8'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((8+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1290)
        if (self.groups['W 8'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((8+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1291)
        if (self.groups['W 8'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1292)
        if (self.groups['W 8'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((8+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1293)
        if (self.groups['W 8'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((8+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1294)
        if (self.groups['W 8'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+8))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1295)
        if (self.groups['W 8'] and
        loop_index == 399):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((8+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1296)
        if (self.groups['W 8'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+800000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1297)
        if (self.groups['W 8'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1298)
        if (self.groups['W 8'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+800000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(1299)
        if (self.groups['W 8'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1300)
        if self.groups['W 8']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1301)
        if (self.groups['W 8'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_waffe1(self, loop_index):
        self.set_event_id(1158)
        if (self.groups['W1'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((1+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1159)
        if (self.groups['W1'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((1+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1160)
        if (self.groups['W1'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1161)
        if (self.groups['W1'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((1+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1162)
        if (self.groups['W1'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((1+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1163)
        if (self.groups['W1'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+1))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1164)
        if (self.groups['W1'] and
        loop_index == 479):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((1+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1165)
        if (self.groups['W1'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1166)
        if (self.groups['W1'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1167)
        if (self.groups['W1'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(1168)
        if (self.groups['W1'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1169)
        if self.groups['W1']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1170)
        if (self.groups['W1'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_kick_timeout2(self, loop_index):
        self.set_event_id(172)
        if self.groups['Server main']:
            self.get(Moo2_447).SelectSocket(loop_index+1)
        self.set_event_id(173)
        if (self.groups['Server main'] and
        to_number(self.get(Timeout1_448).get_line(loop_index+1)) >= 4):
            self.get(Moo2_447).delete_socket()
        pass
    
    def loop_waffe3(self, loop_index):
        self.set_event_id(1194)
        if (self.groups['W3'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Strafing_219).values[5] = 3
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Strafing_219).values[6] = 0
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1195)
        if (self.groups['W3'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Strafing_219).AddToAlterable(5, 1)
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Strafing_219).values[6] = 0
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1196)
        if (self.groups['W3'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1197)
        if (self.groups['W3'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Strafing_219).AddToAlterable(5, 1)
            self.get(Active7_195).destroy()
            self.get(Strafing_219).values[6] = 0
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1198)
        if (self.groups['W3'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Strafing_219).AddToAlterable(5, 1)
            self.get(Active7_195).destroy()
            self.get(Strafing_219).values[6] = 0
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1199)
        if (self.groups['W3'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Strafing_219).AddToAlterable(5, 1)
            self.get(Active7_195).destroy()
            self.get(Strafing_219).values[6] = 0
            return False
        self.set_event_id(1200)
        if (self.groups['W3'] and
        loop_index == 399):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Strafing_219).AddToAlterable(5, 1)
            self.get(Active7_195).destroy()
            self.get(Strafing_219).values[6] = 0
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1201)
        if (self.groups['W3'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Strafing_219).AddToAlterable(5, 1)
            self.get(Active7_195).destroy()
            self.get(Fusssoldat2_194).AddToAlterable(19, immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0))
            return False
        self.set_event_id(1202)
        if (self.groups['W3'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1203)
        if (self.groups['W3'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Strafing_219).AddToAlterable(5, 1)
            self.get(Fusssoldat2_194).AddToAlterable(19, immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, immediate_compare(self.get(Fusssoldat2_194).values[19], '<', 300, self.get(Active7_195).values[3]+300, self.get(Active7_195).values[3]), 0))
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1204)
        if (self.groups['W3'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1205)
        if self.groups['W3']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1208)
        if (self.groups['W3'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_waffe2(self, loop_index):
        self.set_event_id(1176)
        if (self.groups['W2'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((2+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1177)
        if (self.groups['W2'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((2+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1178)
        if (self.groups['W2'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1179)
        if (self.groups['W2'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((2+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1180)
        if (self.groups['W2'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((2+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1181)
        if (self.groups['W2'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+2))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1182)
        if (self.groups['W2'] and
        loop_index == 499):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((2+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1183)
        if (self.groups['W2'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1300000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1184)
        if (self.groups['W2'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1185)
        if (self.groups['W2'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+1300000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(1186)
        if (self.groups['W2'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1187)
        if self.groups['W2']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1188)
        if (self.groups['W2'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_waffe5(self, loop_index):
        self.set_event_id(1235)
        if (self.groups['W 5'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((5+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1236)
        if (self.groups['W 5'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((5+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1237)
        if (self.groups['W 5'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1238)
        if (self.groups['W 5'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((5+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1239)
        if (self.groups['W 5'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((5+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1240)
        if (self.groups['W 5'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+5))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1241)
        if (self.groups['W 5'] and
        loop_index == 799):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((5+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1242)
        if (self.groups['W 5'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+500000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1243)
        if (self.groups['W 5'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1244)
        if (self.groups['W 5'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+500000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(1245)
        if (self.groups['W 5'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1246)
        if self.groups['W 5']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1247)
        if (self.groups['W 5'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_waffe4(self, loop_index):
        self.set_event_id(1214)
        if (self.groups['W 4'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((4+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1215)
        if (self.groups['W 4'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((4+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1216)
        if (self.groups['W 4'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1217)
        if (self.groups['W 4'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((4+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1218)
        if (self.groups['W 4'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((4+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1219)
        if (self.groups['W 4'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+4))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1220)
        if (self.groups['W 4'] and
        loop_index == 419):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((4+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1221)
        if (self.groups['W 4'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+400000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1222)
        if (self.groups['W 4'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1223)
        if (self.groups['W 4'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+400000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(1224)
        if (self.groups['W 4'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1225)
        if self.groups['W 4']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1226)
        if (self.groups['W 4'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_timeout(self, loop_index):
        self.set_event_id(165)
        if self.groups['Server main']:
            self.get(Moo_181).SelectSocket(loop_index+1)
            self.get(Moo_181).set_property('timeout', str(to_number(self.get(Moo_181).get_property('timeout'))+1))
        pass
    
    def loop_waffe6(self, loop_index):
        self.set_event_id(1253)
        if (self.groups['W 6'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((6+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1254)
        if (self.groups['W 6'] and
        loop_index == 0 and
        select(self.get(TestShoot_306).OnCollision(qualifier_2)) and
        select(self.get(Fusssoldat_193).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).values[22] = 1
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(TestShoot_306).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((6+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1255)
        if (self.groups['W 6'] and
        loop_index == 1):
            self.get(TestShoot_306).destroy()
        self.set_event_id(1256)
        if (self.groups['W 6'] and
        select(self.get(Active7_195).OnCollision(qualifier_6))):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((6+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1257)
        if (self.groups['W 6'] and
        select(self.get(Active7_195).OnCollision(qualifier_2)) and
        select(self.get(qualifier_2).values.get(14, 0) <= self.get(Active7_195).values[14]) and
        select(self.get(qualifier_2).values.get(9, 0) < self.get(Active7_195).values[9]) and
        select(self.get(Active7_195).values.get(9, 0) >= self.get(qualifier_2).values[9])):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((6+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1258)
        if (self.groups['W 6'] and
        select(self.get(Active7_195).OutsidePlayfield()) and
        select(self.get(Fusssoldat_193).visible)):
            self.get(Active7_195).destroy()
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+6))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return False
        self.set_event_id(1259)
        if (self.groups['W 6'] and
        loop_index == 449):
            self.create_object(HitBack_198, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active7_195).x + 0, self.get(Active7_195).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active7_195)', 'create_object': 'Splitter_202'}
            self.get(Active7_195).destroy()
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((6+100*self.get(Active7_195).x+self.get(Active7_195).y*100000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
        self.set_event_id(1260)
        if (self.groups['W 6'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = self.get(Active7_195).values[3]/5
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+600000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(1261)
        if (self.groups['W 6'] and
        select(self.get(Active7_195).OnCollision(Fusssoldat2_194)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 0)):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1262)
        if (self.groups['W 6'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).values[3] = self.get(Active7_195).values[3]*3
            self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.get(Fusssoldat2_194).values[6] = (self.get(Active7_195).values[3]/5)*-1
            self.get(Active7_195).values[3] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Active7_195).values[3], 0)
            self.get(Fusssoldat2_194).values[24] -= self.get(Active7_195).values[3]
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[5] = 1
            return False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((300+self.get(Active7_195).values[3]+self.get(Fusssoldat2_194).values[12]*1000+600000))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Active7_195).destroy()
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(1263)
        if (self.groups['W 6'] and
        select(self.get(Active7_195).OnCollision(Head_441)) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
        select(self.get(Active7_195).values.get(22, 0) != 1) and
        select(self.get(Active7_195).values.get(7, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0])):
            self.get(Active7_195).destroy()
            return False
        self.set_event_id(1264)
        if self.groups['W 6']:
            self.get(Active7_195).set_position(x = self.get(Active7_195).values[0]*(loop_index+1)+self.get(Active7_195).values[23])
            self.get(Active7_195).set_position(y = self.get(Active7_195).values[1]*(loop_index+1)+self.get(Active7_195).values[24])
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
        self.set_event_id(1265)
        if (self.groups['W 6'] and
        loop_index%50 == 0):
            self.get(Active7_195).values[3] -= 1
        pass
    
    def loop_ban(self, loop_index):
        self.set_event_id(92)
        if (self.groups['Server main'] and
        self.get(StringParser_43).get_element(-1 + (loop_index+1)) == self.get(Checkip_395).text):
            self.get(Fusssoldat_193).flags[31] = True
            return False
        pass
    
    def loop_testhide(self, loop_index):
        self.set_event_id(616)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat2_194).values.get(21, 0) == loop_index) and
        select(self.get(Fusssoldat2_194).IsOverlapping(SmokeExp_460)) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        select(self.get(NameTag3_433).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
            self.get(NameTag2_429).set_visible(False)
            self.get(NameTag2_429).values[23] = 25
            self.get(NameTag3_433).set_visible(False)
            self.get(NameTag3_433).values[23] = 25
        pass
    
    def loop_c4dmg(self, loop_index):
        self.set_event_id(113)
        if self.groups['Server main']:
            self.get(Msg_427).set_value('122'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+self.get(Reclist_426).get_line(loop_index+1))
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        pass
    
    def function_216(self, int_arg = None):
        self.set_event_id(355)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(356)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.create_object(Nade2_459, -34, 174) # {'y': 174, 'x': -34, 'create_object': 'Nade2_459'}
            self.get(Nade2_459).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Nade2_459).set_position(x = (to_number(self.get(Msg_427).text)%1000000)/1000)
            self.get(Nade2_459).set_position(y = to_number(self.get(Msg_427).text)/1000000)
            self.get(Nade2_459).movement.set_speed((to_number(self.get(Msg_427).text)%1000)/100+10)
            self.get(Fusssoldat2_194).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Nade2_459).values[23] = 1
        pass
    
    def function_217(self, int_arg = None):
        self.set_event_id(357)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(358)
        if (self.groups['Both'] and
        self.get(Msg_427).text == '0' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
            self.get(Chatting_355).values[1] = 0
        self.set_event_id(359)
        if (self.groups['Both'] and
        self.get(Msg_427).text == '1' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
            self.get(Chatting_355).values[1] = 0
            self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.get(Fusssoldat2_194).values[7] -= 1
        pass
    
    def function_clrec(self, int_arg = None):
        self.set_event_id(178)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(decrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        self.set_event_id(179)
        if self.groups['Client main']:
            self.get(NotID_430).set_value(to_number(mid_string(self.get(Msg_427).text, 3, 2)))
            getattr(self, "function_" + left_string(self.get(Msg_427).text, 3))()
        pass
    
    def function_215(self, int_arg = None):
        self.set_event_id(290)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
        self.set_event_id(291)
        if (self.groups['Client main'] and
        self.get(Msg_427).text == 'police'):
            PlaySample(start1_22)
            self.get(ScorePolice_368).add_value(1)
            self.get(PoliceWin_362).set_position(400, 300) # {'y': 300, 'x': 400}
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(Counter3_246).set_value(0)
        self.set_event_id(292)
        if (self.groups['Client main'] and
        self.get(Msg_427).text == 'terror'):
            PlaySample(start1_22)
            self.get(TerrorWin_363).set_position(400, 300) # {'y': 300, 'x': 400}
            self.get(ScoreTerror_369).add_value(1)
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(Counter3_246).set_value(0)
        pass
    
    def function_122(self, int_arg = None):
        self.set_event_id(260)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(StringParser_43).set_value(self.get(Msg_427).text)
        self.set_event_id(261)
        if self.groups['Client main']:
            self.create_object(Destroy_375, -167, 228) # {'y': 228, 'x': -167, 'create_object': 'Destroy_375'}
            self.get(Destroy_375).set_visible(False)
            self.get(Destroy_375).set_position(x = to_number(self.get(StringParser_43).get_element(-1 + 1)))
            self.get(Destroy_375).set_position(y = to_number(self.get(StringParser_43).get_element(-1 + 2)))
        pass
    
    def function_213(self, int_arg = None):
        self.set_event_id(160)
        if self.groups['Server main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(161)
        if (self.groups['Server main'] and
        self.get(Msg_427).text == 'police' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
            self.get(Fusssoldat2_194).values[18] = 1
            self.get(Fusssoldat2_194).values[25] = 0
            self.add_hud_line(self.get(NameTag2_429).get_text()+' joined the police')
            for loop_index in xrange(self.get(Players_317).get_value()):
                if self.loop_team_count(loop_index) == False: break
        self.set_event_id(162)
        if (self.groups['Server main'] and
        self.get(Msg_427).text == 'terror' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
            self.get(Fusssoldat2_194).values[18] = 2
            self.get(Fusssoldat2_194).values[25] = 0
            self.add_hud_line(self.get(NameTag2_429).get_text()+' joined the terrorists')
            for loop_index in xrange(self.get(Players_317).get_value()):
                if self.loop_team_count(loop_index) == False: break
        self.set_event_id(284)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
            self.get(DurchlaufChat_245).set_value(0)
        self.set_event_id(285)
        if (self.groups['Client main'] and
        self.get(Msg_427).text == 'police' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
            self.get(Fusssoldat2_194).values[18] = 1
            self.get(Fusssoldat_193).values[22] = 0
            self.add_hud_line(self.get(NameTag2_429).get_text()+' joined the police')
        self.set_event_id(286)
        if (self.groups['Client main'] and
        self.get(Msg_427).text == 'terror' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
            self.get(Fusssoldat2_194).values[18] = 2
            self.get(Fusssoldat_193).values[22] = 0
            self.add_hud_line(self.get(NameTag2_429).get_text()+' joined the terrorists')
        pass
    
    def function_210(self, int_arg = None):
        self.set_event_id(262)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
        self.set_event_id(263)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 1) and
        select(self.get(DM_412).get_value() == 1)):
            self.get(ScoreTerror_369).add_value(self.get(DM_412).get_value())
        self.set_event_id(264)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 2) and
        select(self.get(DM_412).get_value() == 1)):
            self.get(ScorePolice_368).add_value(self.get(DM_412).get_value())
        self.set_event_id(265)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 0)):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.create_object(Obj2Die_199, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Obj2Die_199'}
            self.get(Obj2Die_199).values[9] = self.get(Obj2Die_199).y
            self.get(Obj2Die_199).values[6] = 8
        self.set_event_id(266)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.create_object(Obj6Die_341, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Obj6Die_341'}
            self.get(Obj6Die_341).values[9] = self.get(Obj6Die_341).y
            self.get(Obj6Die_341).values[6] = 8
        self.set_event_id(267)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == 2)):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.create_object(Obj5Die_340, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Obj5Die_340'}
            self.get(Obj5Die_340).values[9] = self.get(Obj5Die_340).y
            self.get(Obj5Die_340).values[6] = 8
        self.set_event_id(268)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        self.get(VisibleId_424).get_value() != to_number(self.get(Msg_427).text)%100 and
        to_number(self.get(Msg_427).text)/10000 == 1):
            self.get(Active2_254).BringToBack()
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Strafing2_220).values[25] = 0
            self.get(Fusssoldat2_194).flags[1] = False
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('die.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(269)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Fusssoldat2_194).values.get(18, 0) != self.get(Fusssoldat_193).values[8]+(10*(1-self.get(Mode_344).get_value()))) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        self.get(VisibleId_424).get_value() == to_number(self.get(Msg_427).text)%100 and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(NameTag2_429).values.get(0, 0) == (to_number(self.get(Msg_427).text)%10000)/100)):
            self.get(Active2_254).BringToBack()
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You killed '+self.get(NameTag2_429).get_text())
            self.groups['Timer'] = True
            self.get(Frags_209).add_value(1)
            self.get(SkillCounter_211).add_value(1)
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.get(Money_366).add_value(500)
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Strafing2_220).values[25] = 0
            self.get(SvrKills2_32).add_value(1)
            self.get(SvrPoints2_34).add_value(self.get(Fusssoldat2_194).get_flag(1))
            self.get(Fusssoldat2_194).flags[1] = False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return
            self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+500))
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('die.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(270)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Fusssoldat2_194).values.get(18, 0) != self.get(Fusssoldat_193).values[8]+(10*(1-self.get(Mode_344).get_value()))) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        self.get(VisibleId_424).get_value() == to_number(self.get(Msg_427).text)%100 and
        to_number(self.get(Msg_427).text)/10000 == 2 and
        select(self.get(NameTag2_429).values.get(0, 0) == (to_number(self.get(Msg_427).text)%10000)/100)):
            self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You killed '+self.get(NameTag2_429).get_text())
            self.groups['Timer'] = True
            self.get(Frags_209).add_value(1)
            self.get(SkillCounter_211).add_value(1)
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
            self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.get(Money_366).add_value(500)
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Strafing2_220).values[25] = 0
            self.get(SvrKills2_32).add_value(1)
            self.get(SvrPoints2_34).add_value(self.get(Fusssoldat2_194).get_flag(1))
            self.get(Fusssoldat2_194).flags[1] = False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return
            self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+500))
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('burn.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(271)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        self.get(VisibleId_424).get_value() != to_number(self.get(Msg_427).text)%100 and
        to_number(self.get(Msg_427).text)/10000 == 2):
            self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
            self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Strafing2_220).values[25] = 0
            self.get(Fusssoldat2_194).flags[1] = False
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('burn.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(272)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == self.get(Fusssoldat_193).values[8]) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        self.get(VisibleId_424).get_value() == to_number(self.get(Msg_427).text)%100 and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(Active2_254).BringToBack()
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You killed a teammate')
            self.groups['Timer'] = True
            self.get(Frags_209).subtract_value(2)
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.get(Money_366).set_value(0)
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Strafing2_220).values[25] = 0
            self.get(SvrKills2_32).subtract_value(2)
            self.get(Fusssoldat2_194).flags[1] = False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return
            self.get(String31_437).set_value('0')
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('die.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(273)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%10000)/100) and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == self.get(Fusssoldat_193).values[8]) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
        self.get(VisibleId_424).get_value() == to_number(self.get(Msg_427).text)%100 and
        to_number(self.get(Msg_427).text)/10000 == 2 and
        select(self.get(Mode_344).get_value() == 1)):
            self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
            self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You killed a teammate')
            self.groups['Timer'] = True
            self.get(Frags_209).subtract_value(2)
            self.get(Fusssoldat2_194).values[25] = 0
            self.get(Fusssoldat2_194).values[15] = 0
            self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
            self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.get(Money_366).set_value(0)
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Strafing2_220).values[25] = 0
            self.get(SvrKills2_32).subtract_value(2)
            self.get(Fusssoldat2_194).flags[1] = False
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return
            self.get(String31_437).set_value('0')
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('burn.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(274)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
        select(self.get(DM_412).get_value() == 1)):
            self.get(ScoreTerror_369).add_value(self.get(DM_412).get_value())
        self.set_event_id(275)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
        select(self.get(DM_412).get_value() == 1)):
            self.get(ScorePolice_368).add_value(self.get(DM_412).get_value())
        self.set_event_id(276)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 0)):
            self.create_object(Obj1Die_255, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Obj1Die_255'}
            self.get(Obj1Die_255).values[9] = self.get(Obj1Die_255).y
            self.get(Obj1Die_255).values[6] = 8
        self.set_event_id(277)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1)):
            self.create_object(Obj3Die_338, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Obj3Die_338'}
            self.get(Obj3Die_338).values[9] = self.get(Obj3Die_338).y
            self.get(Obj3Die_338).values[6] = 8
        self.set_event_id(278)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2)):
            self.create_object(Obj4Die_339, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Obj4Die_339'}
            self.get(Obj4Die_339).values[9] = self.get(Obj4Die_339).y
            self.get(Obj4Die_339).values[6] = 8
        self.set_event_id(279)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        select(self.get(DM_412).get_value() == 1)):
            self.get(Respawn_201).set_visible(True)
            self.get(String2_200).set_visible(True)
        self.set_event_id(280)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() != to_number(self.get(Msg_427).text)%100 and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        to_number(self.get(Msg_427).text)/10000 == 1 and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == to_number(self.get(Msg_427).text)%100) and
        select(self.get(NameTag2_429).values.get(0, 0) == to_number(self.get(Msg_427).text)%100)):
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You were killed by '+self.get(NameTag2_429).get_text())
            self.groups['Timer'] = True
            self.players[0].set_ignore(True)
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.get(Fusssoldat_193).values[12] = 0
            self.get(Fusssoldat_193).values[14] = 0
            self.get(Fusssoldat_193).values[7] = 0
            self.get(Fusssoldat_193).values[5] = 0
            self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).BringToBack()
            self.get(Fusssoldat2_194).BringToBack()
            self.get(ActiveObject1_218).BringToBack()
            self.get(Active6_214).set_visible(False)
            self.get(SkillCounter_211).set_value(0)
            self.get(Deaths_210).add_value(1)
            self.get(Oben_239).set_visible(False)
            self.get(Unten_240).set_visible(False)
            self.get(Rechts_241).set_visible(False)
            self.get(Links_242).set_visible(False)
            self.get(Counter3_246).set_value(0)
            self.groups['Weapon Change'] = True
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(SvrDeaths2_33).add_value(1)
            return
            self.get(Snipercounter_438).set_value(0)
            SoundAutoPlay('die.wav')
        self.set_event_id(281)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == to_number(self.get(Msg_427).text)%100 and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        to_number(self.get(Msg_427).text)/10000 == 1):
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You have committed suicide')
            self.groups['Timer'] = True
            self.players[0].set_ignore(True)
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.get(Fusssoldat_193).values[12] = 0
            self.get(Fusssoldat_193).values[14] = 0
            self.get(Fusssoldat_193).values[7] = 0
            self.get(Fusssoldat_193).values[5] = 0
            self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).BringToBack()
            self.get(Fusssoldat2_194).BringToBack()
            self.get(ActiveObject1_218).BringToBack()
            self.get(Active6_214).set_visible(False)
            self.get(SkillCounter_211).set_value(0)
            self.get(Deaths_210).add_value(1)
            self.get(Oben_239).set_visible(False)
            self.get(Unten_240).set_visible(False)
            self.get(Rechts_241).set_visible(False)
            self.get(Links_242).set_visible(False)
            self.get(Frags_209).subtract_value(1)
            self.get(Counter3_246).set_value(0)
            self.groups['Weapon Change'] = True
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(SvrKills2_32).subtract_value(1)
            self.get(SvrDeaths2_33).add_value(1)
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            return
            self.get(Snipercounter_438).set_value(0)
            SoundAutoPlay('die.wav')
        self.set_event_id(282)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() != to_number(self.get(Msg_427).text)%100 and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        to_number(self.get(Msg_427).text)/10000 == 2 and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == to_number(self.get(Msg_427).text)%100) and
        select(self.get(NameTag2_429).values.get(0, 0) == to_number(self.get(Msg_427).text)%100)):
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You were killed by '+self.get(NameTag2_429).get_text())
            self.groups['Timer'] = True
            self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
            self.players[0].set_ignore(True)
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.get(Fusssoldat_193).values[12] = 0
            self.get(Fusssoldat_193).values[14] = 0
            self.get(Fusssoldat_193).values[7] = 0
            self.get(Fusssoldat_193).values[5] = 0
            self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).BringToBack()
            self.get(Fusssoldat2_194).BringToBack()
            self.get(ActiveObject1_218).BringToBack()
            self.get(Active6_214).set_visible(False)
            self.get(SkillCounter_211).set_value(0)
            self.get(Deaths_210).add_value(1)
            self.get(Oben_239).set_visible(False)
            self.get(Unten_240).set_visible(False)
            self.get(Rechts_241).set_visible(False)
            self.get(Links_242).set_visible(False)
            self.get(Counter3_246).set_value(0)
            self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
            self.groups['Weapon Change'] = True
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(SvrDeaths2_33).add_value(1)
            return
            self.get(Snipercounter_438).set_value(0)
            SoundAutoPlay('burn.wav')
        self.set_event_id(283)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == to_number(self.get(Msg_427).text)%100 and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%10000)/100 and
        to_number(self.get(Msg_427).text)/10000 == 2):
            self.get(Fusssoldat_193).values[10] = 0
            self.get(Killed_203).set_visible(True)
            self.get(Killed_203).set_value('You have committed suicide')
            self.groups['Timer'] = True
            self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
            self.players[0].set_ignore(True)
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.get(Fusssoldat_193).values[12] = 0
            self.get(Fusssoldat_193).values[14] = 0
            self.get(Fusssoldat_193).values[7] = 0
            self.get(Fusssoldat_193).values[5] = 0
            self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).BringToBack()
            self.get(Fusssoldat2_194).BringToBack()
            self.get(ActiveObject1_218).BringToBack()
            self.get(Active6_214).set_visible(False)
            self.get(SkillCounter_211).set_value(0)
            self.get(Deaths_210).add_value(1)
            self.get(Oben_239).set_visible(False)
            self.get(Unten_240).set_visible(False)
            self.get(Rechts_241).set_visible(False)
            self.get(Links_242).set_visible(False)
            self.get(Frags_209).subtract_value(1)
            self.get(Counter3_246).set_value(0)
            self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
            self.groups['Weapon Change'] = True
            self.groups['Shop'] = False
            self.get(ShopList_370).set_visible(False)
            self.get(ShopListPrice_371).set_visible(False)
            self.get(Shop1Blitter_372).set_visible(False)
            self.get(Shop2Blitter_373).set_visible(False)
            self.get(Shop1Blitter2_385).set_visible(False)
            self.get(Shop1Blitter3_386).set_visible(False)
            self.get(SvrKills2_32).subtract_value(1)
            self.get(SvrDeaths2_33).add_value(1)
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            self.get(Snipercounter_438).set_value(0)
            SoundAutoPlay('burn.wav')
        pass
    
    def function_211(self, int_arg = None):
        self.set_event_id(346)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(347)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(7, 0) < to_number(self.get(Msg_427).text))):
            self.get(Fusssoldat2_194).flags[1] = True
        self.set_event_id(348)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).values[7] = to_number(self.get(Msg_427).text)
        pass
    
    def function_214(self, int_arg = None):
        self.set_event_id(287)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
        select(self.get(PoliceSpawn_345).PickRandom()) and
        negate(self.groups['Map change'])):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(Strafing_219).set_position(self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)'}
            self.get(Fusssoldat_193).set_visible(True)
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.get(TrackX_268).set_value(self.get(Strafing_219).x)
            self.get(TrackY_269).set_value(self.get(Strafing_219).y)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Killed_203).set_value('')
            self.get(Killed_203).set_visible(False)
            self.function_write_shop()
            self.groups['reset standard'] = True
            self.groups['Shop'] = True
            self.get(ShopList_370).set_visible(True)
            self.get(ShopListPrice_371).set_visible(True)
            self.get(Money_366).add_value(1500)
            self.get(PingCounter_232).set_value(0)
            self.get(Counter3_246).set_value(0)
            self.get(Shop1Blitter_372).set_visible(True)
            self.get(Shop2Blitter_373).set_visible(True)
            self.players[0].set_ignore(True)
            self.get(Shop1Blitter2_385).set_visible(True)
            self.get(Shop1Blitter3_386).set_visible(True)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Active9_222).values[7] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(NotID_430).set_value(0)
            self.function_sendall()
            self.function_csmup()
            self.get(Msg_427).set_value('110'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
            self.function_sendall()
            self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+1500))
            self.get(Snipercounter_438).set_value(0)
        self.set_event_id(288)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
        select(self.get(TerrorSpawn_346).PickRandom()) and
        negate(self.groups['Map change'])):
            self.get(Fusssoldat_193).values[5] = 100
            self.get(Strafing_219).set_position(self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)'}
            self.get(Fusssoldat_193).set_visible(True)
            self.get(Strafing_219).movement.stop()
            self.get(Fusssoldat_193).values[14] = 1
            self.get(TrackX_268).set_value(self.get(Strafing_219).x)
            self.get(TrackY_269).set_value(self.get(Strafing_219).y)
            self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
            self.get(Oben_239).set_visible(True)
            self.get(Unten_240).set_visible(True)
            self.get(Rechts_241).set_visible(True)
            self.get(Links_242).set_visible(True)
            self.get(Strafing_219).values[18] = -1
            self.create_object(MagicExplode3_212, self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)', 'create_object': 'MagicExplode3_212'}
            self.get(SkillCounter_211).set_value(0)
            self.get(Killed_203).set_value('')
            self.get(Killed_203).set_visible(False)
            self.function_write_shop()
            self.groups['reset standard'] = True
            self.groups['Shop'] = True
            self.get(ShopList_370).set_visible(True)
            self.get(ShopListPrice_371).set_visible(True)
            self.get(Money_366).add_value(1500)
            self.get(PingCounter_232).set_value(0)
            self.get(Counter3_246).set_value(0)
            self.get(Shop1Blitter_372).set_visible(True)
            self.get(Shop2Blitter_373).set_visible(True)
            self.players[0].set_ignore(True)
            self.get(Shop1Blitter2_385).set_visible(True)
            self.get(Shop1Blitter3_386).set_visible(True)
            self.get(Fusssoldat_193).values[15] = 0
            self.get(Active9_222).values[7] = 0
            self.get(Oben_239).restore_animation()
            self.get(Unten_240).restore_animation()
            self.get(Rechts_241).restore_animation()
            self.get(Links_242).restore_animation()
            self.get(NotID_430).set_value(0)
            self.function_sendall()
            self.function_csmup()
            self.get(Msg_427).set_value('110'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
            self.function_sendall()
            self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+1500))
            self.get(Snipercounter_438).set_value(0)
        self.set_event_id(289)
        if self.groups['Client main']:
            self.get(Gaswolke_215).destroy()
            self.get(Nade_458).destroy()
            self.get(Exp_247).destroy()
            self.get(PoliceWin_362).set_position(-27, 672) # {'y': 672, 'x': -27}
            self.get(TerrorWin_363).set_position(-27, 672) # {'y': 672, 'x': -27}
            self.get(C4_374).destroy()
            self.get(WallDestroyed_376).destroy()
            self.get(qualifier_6).restore_animation()
            self.get(Box_287).restore_animation()
            self.get(BoxDestroyed_377).destroy()
            self.get(Nade2_459).destroy()
            self.get(FlashTime_381).set_value(0)
            self.get(GrenadeSpot_398).destroy()
            self.get(Pipeline_403).restore_animation()
            self.get(PipelineDestroyed_411).destroy()
            self.get(PoliceCar_275).restore_animation()
            self.get(PoliceCar2_276).restore_animation()
            self.get(Reclist_426).reset()
            self.get(Molotov_450).destroy()
            self.get(Active17_451).destroy()
            self.get(P1_452).destroy()
            self.get(FlameDmg_456).destroy()
            self.get(BigflameDmg_457).destroy()
            self.get(SmokeExp_460).destroy()
        pass
    
    def function_218(self, int_arg = None):
        self.set_event_id(293)
        if (self.groups['Client main'] and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.add_hud_line('Server restarts game')
            self.get(ScorePolice_368).set_value(0)
            self.get(ScoreTerror_369).set_value(0)
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.groups['Weapon Change'] = True
            self.get(Money_366).set_value(0)
            self.get(Active6_214).set_visible(False)
            self.get(Fusssoldat_193).values[12] = 0
            self.get(FlashTime_381).set_value(0)
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Chatting_355).values[1] = 0
            self.get(String31_437).set_value('0')
        pass
    
    def function_219(self, int_arg = None):
        self.set_event_id(360)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(361)
        if (self.groups['Both'] and
        self.get(Msg_427).text == '0' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).values[18] = 0
        self.set_event_id(362)
        if (self.groups['Both'] and
        self.get(Msg_427).text == '1' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).values[18] = 1
        self.set_event_id(363)
        if (self.groups['Both'] and
        self.get(Msg_427).text == '2' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).values[18] = 2
        pass
    
    def function_115(self, int_arg = None):
        self.set_event_id(156)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).values[13] = 0
        pass
    
    def function_114(self, int_arg = None):
        self.set_event_id(247)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-3))
        self.set_event_id(248)
        if self.groups['Client main']:
            self.get(StringParser_43).set_value(self.get(Msg_427).text)
            self.get(ScorePolice_368).set_value(to_number(self.get(StringParser_43).get_element(-1 + 1)))
            self.get(ScoreTerror_369).set_value(to_number(self.get(StringParser_43).get_element(-1 + 2)))
        pass
    
    def function_117(self, int_arg = None):
        self.set_event_id(251)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
        self.set_event_id(252)
        if (self.groups['Client main'] and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Chatting_355).values[1] = 0
        self.set_event_id(253)
        if (self.groups['Client main'] and
        self.get(RealName_390).text == self.get(Msg_427).text):
            self.get(ErrorMsg_244).set_value('Kicked by admin')
            self.groups['Disconnect'] = True
            self.get(FlashTime_381).set_value(0)
        self.set_event_id(254)
        if (self.groups['Client main'] and
        self.get(Msg_427).text == str(self.get(VisibleId_424).get_value())):
            self.get(ErrorMsg_244).set_value('Kicked by admin')
            self.groups['Disconnect'] = True
            self.get(FlashTime_381).set_value(0)
        pass
    
    def function_116(self, int_arg = None):
        self.set_event_id(249)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-3))
        self.set_event_id(250)
        if (self.groups['Client main'] and
        self.get(Msg_427).text+'.sdo' != self.get(ChosedMapWithoutPath_126).text):
            self.values[12] = immediate_compare(self.get_global_value(12), '=', 2, 1, 0)
            self.get(FlashTime_381).set_value(0)
            self.set_frame(4)
        pass
    
    def function_110(self, int_arg = None):
        self.set_event_id(123)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == to_number(mid_string(self.get(Msg_427).text, 3, 2)))):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '110'))
            self.get(Fusssoldat2_194).values[24] = 100
            self.get(Fusssoldat2_194).values[25] = 1
            self.get(Fusssoldat2_194).values[15] = 0
        self.set_event_id(216)
        if (self.groups['Client main'] and
        select(self.get(Mode_344).get_value() == 0)):
            self.get(Ping_233).set_value(self.get(PingCounter_232).get_value())
            for loop_index in xrange(100):
                if self.loop_spawn(loop_index) == False: break
        self.set_event_id(217)
        if (self.groups['Client main'] and
        select(self.get(Mode_344).get_value() == 1) and
        select(self.get(DM_412).get_value() == 0)):
            self.get(Ping_233).set_value(self.get(PingCounter_232).get_value())
        self.set_event_id(218)
        if (self.groups['Client main'] and
        select(self.get(DM_412).get_value() == 1) and
        select(self.get(Mode_344).get_value() == 1) and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1)):
            self.get(Ping_233).set_value(self.get(PingCounter_232).get_value())
            for loop_index in xrange(100):
                if self.loop_spawn_p(loop_index) == False: break
        self.set_event_id(219)
        if (self.groups['Client main'] and
        select(self.get(DM_412).get_value() == 1) and
        select(self.get(Mode_344).get_value() == 1) and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2)):
            self.get(Ping_233).set_value(self.get(PingCounter_232).get_value())
            for loop_index in xrange(100):
                if self.loop_spawn_t(loop_index) == False: break
        pass
    
    def function_113(self, int_arg = None):
        self.set_event_id(149)
        if self.groups['Server main']:
            self.get(NotID_430).set_value(to_number(mid_string(self.get(Msg_427).text, 3, 2)))
            self.get(Csm_432).set_value(to_number(right_string(self.get(Msg_427).text, 1)))
            self.function_hitdmg()
            self.get(Temp2_454).set_value(self.get(Msg_427).text)
        self.set_event_id(150)
        if self.groups['Server main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(151)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000):
            SoundAutoPlay('hit.wav')
        self.set_event_id(152)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        self.players[0].lives == 5 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= to_number(self.get(Msg_427).text)%1000
            self.get(Fusssoldat_193).values[25] = self.get(Fusssoldat2_194).values[12]
            self.get(Fusssoldat_193).values[16] = to_number(self.get(Msg_427).text)/1000000
            self.get(Fusssoldat_193).values[6] = 10
        self.set_event_id(153)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        self.players[0].lives != 5 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= to_number(self.get(Msg_427).text)%1000
            self.get(Fusssoldat_193).values[25] = self.get(Fusssoldat2_194).values[12]
            self.get(Fusssoldat_193).values[16] = to_number(self.get(Msg_427).text)/100000
            self.get(Fusssoldat_193).values[6] = 10
        self.set_event_id(154)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[24] -= to_number(self.get(Msg_427).text)%1000
            self.get(Fusssoldat2_194).values[23] = self.get(NotID_430).get_value()
            self.get(Fusssoldat2_194).values[5] = to_number(self.get(Msg_427).text)/100000
            self.get(Fusssoldat2_194).values[6] = 10
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(155)
        if self.groups['Server main']:
            self.get(Msg_427).set_value(self.get(Temp2_454).text)
            self.function_csm()
            self.function_sendall()
        self.set_event_id(242)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(243)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
            SoundAutoPlay('hit.wav')
        self.set_event_id(244)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        self.players[0].lives == 5 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= to_number(self.get(Msg_427).text)%1000
            self.get(Fusssoldat_193).values[6] = 10
        self.set_event_id(245)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        self.players[0].lives != 5 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= to_number(self.get(Msg_427).text)%1000
            self.get(Fusssoldat_193).values[6] = 10
        self.set_event_id(246)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[6] = 10
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        pass
    
    def function_112(self, int_arg = None):
        self.set_event_id(124)
        if self.groups['Server main']:
            self.get(NotID_430).set_value(to_number(mid_string(self.get(Msg_427).text, 3, 2)))
            self.get(Csm_432).set_value(to_number(right_string(self.get(Msg_427).text, 1)))
            self.function_csm()
            self.function_hitdmg()
            self.function_sendall()
        self.set_event_id(127)
        if self.groups['Server main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(128)
        if (self.groups['Server main'] and
        select(self.get(Strafing2_220).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)/100000 >= 1):
            self.get(Fusssoldat2_194).LookAt({'y': 0, 'x': 0, 'parent': 'self.get(Strafing2_220)'})
        self.set_event_id(129)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        to_number(self.get(Msg_427).text)/100000 >= 1):
            self.get(Fusssoldat2_194).LookAt({'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)'})
        self.set_event_id(130)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 1 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('glock.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(131)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 13 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('ak47.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(132)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 3 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('m3.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(133)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 4 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('deagle.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(134)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 5 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundAutoPlay('sniper.wav')
        self.set_event_id(135)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 6 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('mp5.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(136)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 7 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('g3.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(137)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 8 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('sig.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(138)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 9 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('m4.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(139)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 10 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('galil.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(140)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 11 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('svd.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(141)
        if (self.groups['Server main'] and
        to_number(self.get(Msg_427).text)/100000 == 12 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundAutoPlay('sr60.wav')
        self.set_event_id(142)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 < 300):
            SoundAutoPlay('hit.wav')
        self.set_event_id(143)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 >= 300):
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(144)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 >= 300):
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(145)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        self.players[0].lives == 5 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, to_number(self.get(Msg_427).text)%1000, to_number(self.get(Msg_427).text)%1000-300), 0)
            self.get(Fusssoldat_193).values[25] = self.get(Fusssoldat2_194).values[12]
            self.get(Fusssoldat_193).values[16] = 1
            self.get(Accuracy_238).add_value((to_number(self.get(Msg_427).text)%1000)*3)
            self.get(Fusssoldat_193).values[6] = immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, (to_number(self.get(Msg_427).text)%1000)/5, ((to_number(self.get(Msg_427).text)%1000-300)/5)*-1)
        self.set_event_id(146)
        if (self.groups['Server main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        self.players[0].lives != 5 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, to_number(self.get(Msg_427).text)%1000, to_number(self.get(Msg_427).text)%1000-300), 0)
            self.get(Fusssoldat_193).values[25] = self.get(Fusssoldat2_194).values[12]
            self.get(Fusssoldat_193).values[16] = 1
            self.get(Fusssoldat_193).values[6] = immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, (to_number(self.get(Msg_427).text)%1000)/5, ((to_number(self.get(Msg_427).text)%1000-300)/5)*-1)
        self.set_event_id(147)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 < 300):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[24] -= immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, to_number(self.get(Msg_427).text)%1000, 0)
            self.get(Fusssoldat2_194).values[23] = self.get(Strafing2_220).values[12]
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(Fusssoldat2_194).values[6] = (to_number(self.get(Msg_427).text)%1000)/5
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(148)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 >= 300):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[24] -= immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, to_number(self.get(Msg_427).text)%1000-300, 0)
            self.get(Fusssoldat2_194).values[23] = self.get(Strafing2_220).values[12]
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(Fusssoldat2_194).values[6] = (to_number(self.get(Msg_427).text)%1000-300)/5
        self.set_event_id(220)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(221)
        if (self.groups['Client main'] and
        select(self.get(Strafing2_220).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)/100000 >= 1):
            self.get(Fusssoldat2_194).LookAt({'y': 0, 'x': 0, 'parent': 'self.get(Strafing2_220)'})
        self.set_event_id(222)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        to_number(self.get(Msg_427).text)/100000 >= 1):
            self.get(Fusssoldat2_194).LookAt({'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)'})
        self.set_event_id(223)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 1 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('glock.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(224)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 13 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('ak47.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(225)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 3 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('m3.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(226)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 4 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('deagle.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(227)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 5 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundAutoPlay('sniper.wav')
        self.set_event_id(228)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 6 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('mp5.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(229)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 7 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('g3.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(230)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 8 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('sig.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(231)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 9 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('m4.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(232)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 10 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('galil.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(233)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 11 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('svd.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(234)
        if (self.groups['Client main'] and
        to_number(self.get(Msg_427).text)/100000 == 12 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundAutoPlay('sr60.wav')
        self.set_event_id(235)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 < 300):
            SoundAutoPlay('hit.wav')
        self.set_event_id(236)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 >= 300):
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(237)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 >= 300):
            SoundAutoPlay('headshot'+str(randrange(3)+1)+'.wav')
        self.set_event_id(238)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        self.players[0].lives == 5 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, to_number(self.get(Msg_427).text)%1000, to_number(self.get(Msg_427).text)%1000-300)
            self.get(Accuracy_238).add_value((to_number(self.get(Msg_427).text)%1000)*3)
            self.get(Fusssoldat_193).values[6] = immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, (to_number(self.get(Msg_427).text)%1000)/5, ((to_number(self.get(Msg_427).text)%1000-300)/5)*-1)
        self.set_event_id(239)
        if (self.groups['Client main'] and
        self.get(VisibleId_424).get_value() == (to_number(self.get(Msg_427).text)%100000)/1000 and
        self.players[0].lives != 5 and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat_193).values[5] -= immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, to_number(self.get(Msg_427).text)%1000, to_number(self.get(Msg_427).text)%1000-300)
            self.get(Fusssoldat_193).values[6] = immediate_compare(to_number(self.get(Msg_427).text)%1000, '<', 300, (to_number(self.get(Msg_427).text)%1000)/5, ((to_number(self.get(Msg_427).text)%1000-300)/5)*-1)
        self.set_event_id(240)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 < 300):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[6] = (to_number(self.get(Msg_427).text)%1000)/5
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(241)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(12, 0) == (to_number(self.get(Msg_427).text)%100000)/1000) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%1000 >= 300):
            self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
            self.get(Active2_254).BringToBack()
            self.get(Fusssoldat2_194).values[6] = (to_number(self.get(Msg_427).text)%1000-300)/5
        pass
    
    def function_212(self, int_arg = None):
        self.set_event_id(349)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(350)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 < 32 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).set_direction(to_number(self.get(Msg_427).text)%100)
        self.set_event_id(351)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 >= 32 and
        to_number(self.get(Msg_427).text)%100 < 64 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).set_direction((to_number(self.get(Msg_427).text)%100)-32)
        self.set_event_id(352)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 < 32):
            self.create_object(Nade_458, 4, -60) # {'y': -60, 'x': 4, 'create_object': 'Nade_458'}
            self.get(Nade_458).values[2] = self.get(NotID_430).get_value()
            self.get(Nade_458).values[1] = 1
            self.get(Nade_458).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Nade_458).set_position(x = (to_number(self.get(Msg_427).text)%1000000)/1000)
            self.get(Nade_458).set_position(y = to_number(self.get(Msg_427).text)/1000000)
            self.get(Nade_458).movement.set_speed((to_number(self.get(Msg_427).text)%1000)/100+5)
            self.get(Nade_458).values[9] = 11110000
            self.get(Nade_458).force_animation('User defined 1')
        self.set_event_id(353)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 >= 32 and
        to_number(self.get(Msg_427).text)%100 < 64):
            self.create_object(Nade_458, 4, -60) # {'y': -60, 'x': 4, 'create_object': 'Nade_458'}
            self.get(Nade_458).values[2] = self.get(NotID_430).get_value()
            self.get(Nade_458).values[1] = 2
            self.get(Nade_458).set_direction((to_number(self.get(Msg_427).text)%100)-32)
            self.get(Nade_458).set_position(x = (to_number(self.get(Msg_427).text)%1000000)/1000)
            self.get(Nade_458).set_position(y = to_number(self.get(Msg_427).text)/1000000)
            self.get(Nade_458).movement.set_speed((to_number(self.get(Msg_427).text)%1000)/100+5)
            self.get(Nade_458).values[9] = 11110000
            self.get(Nade_458).force_animation('Stopped')
        self.set_event_id(354)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 >= 64 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.create_object(C4_374, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 10) # {'y': 10, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'C4_374'}
            self.get(C4_374).values[2] = self.get(NotID_430).get_value()
            self.get(C4_374).set_position(x = (to_number(self.get(Msg_427).text)%100000)/100)
            self.get(C4_374).set_position(y = to_number(self.get(Msg_427).text)/100000)
            self.get(C4_374).values[4] = ((to_number(self.get(Msg_427).text)%100)-64)*50
            self.get(C4_374).values[9] = 1000+to_number(self.get(Msg_427).text)/100000
            self.get(Reclist_426).add_line(str(self.get(C4_374).x)+','+str(self.get(C4_374).y))
            SoundAutoPlay('beep.wav')
        pass
    
    def function_hitdmg(self, int_arg = None):
        self.set_event_id(125)
        if (self.groups['Server main'] and
        select(self.get(InvincibleTime_388).get_value() == 0)):
            return
        self.set_event_id(126)
        if self.groups['Server main']:
            self.get(Temp_431).set_value(right_string(self.get(Msg_427).text, 4))
            self.get(Temp_431).set_value(left_string(self.get(Temp_431).text, len(self.get(Temp_431).text)-1))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-4)+immediate_compare(to_number(self.get(Temp_431).text), '<', 300, '000', '300')+str(self.get(Csm_432).get_value()))
        pass
    
    def function_119(self, int_arg = None):
        self.set_event_id(259)
        if self.groups['Client main']:
            self.get(ErrorMsg_244).set_value('You were banned from the server')
            self.groups['Disconnect'] = True
            self.get(FlashTime_381).set_value(0)
        pass
    
    def function_118(self, int_arg = None):
        self.set_event_id(157)
        if self.groups['Server main']:
            self.add_hud_line('IP: '+'self.get(Moo_181).SockGetRemoteIP'+' banned')
            self.get(BanList_393).set_value(self.get(BanList_393).text+','+'self.get(Moo_181).SockGetRemoteIP')
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '119'))
        self.set_event_id(255)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
        self.set_event_id(256)
        if (self.groups['Client main'] and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Chatting_355).values[1] = 0
        self.set_event_id(257)
        if (self.groups['Client main'] and
        self.get(RealName_390).text == self.get(Msg_427).text):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '118'))
        self.set_event_id(258)
        if (self.groups['Client main'] and
        self.get(Msg_427).text == str(self.get(VisibleId_424).get_value())):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '118'))
        pass
    
    def function_write_shop(self, int_arg = None):
        self.set_event_id(744)
        if self.groups['Game']:
            self.get(ShopList_370).set_value('')
            self.get(ShopListPrice_371).set_value('')
            self.get(Shop1Blitter_372).BlitChangeText('')
            self.get(Shop2Blitter_373).BlitChangeText('')
            self.get(Shop1Blitter2_385).BlitChangeText('')
            self.get(Shop1Blitter3_386).BlitChangeText('')
        self.set_event_id(745)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[4] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'1) Desert Eagle'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'1200$'+'\r\n')
        self.set_event_id(746)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[3] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'2) Benelli M1'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'1300$'+'\r\n')
        self.set_event_id(747)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[6] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'3) MP-5'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'1500$'+'\r\n')
        self.set_event_id(748)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[10] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'4) Galil'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'2000$'+'\r\n')
        self.set_event_id(749)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[11] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'5) SVD'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'2300$'+'\r\n')
        self.set_event_id(750)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[2] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'6) AK-47'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'2000$'+'\r\n')
        self.set_event_id(751)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[9] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'7) Colt M4A1'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'2500$'+'\r\n')
        self.set_event_id(752)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[7] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'8) G3A3'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'2800$'+'\r\n')
        self.set_event_id(753)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[12] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'9) SR-60'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'3000$'+'\r\n')
        self.set_event_id(754)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).flags[5] == True)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'0) AW-50 Sniper'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'3800$'+'\r\n')
        self.set_event_id(755)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 4)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'40$'+'\r\n')
        self.set_event_id(756)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 3)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'60$'+'\r\n')
        self.set_event_id(757)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 6)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'50$'+'\r\n')
        self.set_event_id(758)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 10)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'50$'+'\r\n')
        self.set_event_id(759)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 11)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'80$'+'\r\n')
        self.set_event_id(760)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 2)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'75$'+'\r\n')
        self.set_event_id(761)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 9)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'75$'+'\r\n')
        self.set_event_id(762)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 7)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'100$'+'\r\n')
        self.set_event_id(763)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 12)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'75$'+'\r\n')
        self.set_event_id(764)
        if (self.groups['Game'] and
        select(self.get(SecondWeapon_318).get_value() == 5)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'A) Ammo'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'30$'+'\r\n')
        self.set_event_id(765)
        if self.groups['Game']:
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'Q) C4'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'400$'+'\r\n')
        self.set_event_id(766)
        if self.groups['Game']:
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'W) Gas Grenade'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'200$'+'\r\n')
        self.set_event_id(767)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 1)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'E) Flashbang'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'350$'+'\r\n')
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'S) Smoke Grenade'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'300$'+'\r\n')
        self.set_event_id(768)
        if (self.groups['Game'] and
        select(self.get(Fusssoldat_193).values.get(8, 0) == 2)):
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'E) HE Grenade'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'350$'+'\r\n')
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'S) Molotov Cocktail'+'\r\n')
            self.get(ShopListPrice_371).set_value(self.get(ShopListPrice_371).text+'700$'+'\r\n')
        self.set_event_id(769)
        if self.groups['Game']:
            self.get(ShopList_370).set_value(self.get(ShopList_370).text+'Space) Exit')
            self.get(Shop1Blitter_372).BlitChangeText(self.get(ShopList_370).text)
            self.get(Shop2Blitter_373).BlitChangeText(self.get(ShopListPrice_371).text)
            self.get(Shop1Blitter2_385).BlitChangeText(self.get(ShopList_370).text)
            self.get(Shop1Blitter3_386).BlitChangeText(self.get(ShopListPrice_371).text)
        pass
    
    def function_csm(self, int_arg = None):
        self.set_event_id(61)
        if self.groups['Server main']:
            return
        self.set_event_id(62)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(16, 0) > 0)):
            self.get(Fusssoldat2_194).values[16] -= 1
            self.get(Fusssoldat2_194).values[14] = self.get(Csm_432).get_value()
            self.get(Fusssoldat2_194).values[14] = immediate_compare((self.get(Fusssoldat2_194).values[14]+1), '<', 10, (self.get(Fusssoldat2_194).values[14]+1), 0)
            return
        self.set_event_id(63)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(14, 0) > self.get(Csm_432).get_value())):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '107'))
            self.get(Msg_427).set_value(' ')
        self.set_event_id(64)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(14, 0) == self.get(Csm_432).get_value())):
            self.get(Fusssoldat2_194).values[14] = immediate_compare((self.get(Fusssoldat2_194).values[14]+1), '<', 10, (self.get(Fusssoldat2_194).values[14]+1), 0)
        pass
    
    def function_224(self, int_arg = None):
        self.set_event_id(302)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
            self.get(DurchlaufChat_245).set_value(0)
        self.set_event_id(303)
        if self.groups['Client main']:
            self.get(Fusssoldat_193).values[22] = 0
            self.add_hud_line(self.get(Msg_427).text)
        pass
    
    def function_207(self, int_arg = None):
        self.set_event_id(326)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
            self.create_object(AmmoPack_208, 325, -40) # {'y': -40, 'x': 325, 'create_object': 'AmmoPack_208'}
            self.get(AmmoPack_208).values[0] = to_number(right_string(self.get(Msg_427).text, 2))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-2))
            self.get(AmmoPack_208).set_direction(to_number(self.get(Msg_427).text)/1000000)
            self.get(AmmoPack_208).set_position(x = to_number(self.get(Msg_427).text)%1000)
            self.get(AmmoPack_208).set_position(y = (to_number(self.get(Msg_427).text)%1000000)/1000)
            self.get(AmmoPack_208).values[9] = 1000+self.get(AmmoPack_208).y
            self.get(AmmoPack_208).BringToBack()
        pass
    
    def function_223(self, int_arg = None):
        self.set_event_id(298)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
            self.get(C4_374).destroy()
            self.get(Nade2_459).destroy()
            self.get(Nade_458).destroy()
            self.get(Gaswolke_215).destroy()
            self.get(GrenadeSpot_398).destroy()
            self.get(Exp_247).destroy()
            self.get(Molotov_450).destroy()
            self.get(Active17_451).destroy()
            self.get(P1_452).destroy()
            self.get(FlameDmg_456).destroy()
            self.get(BigflameDmg_457).destroy()
            self.get(SmokeExp_460).destroy()
        self.set_event_id(299)
        if self.groups['Client main']:
            self.get(StringParser_43).set_value(self.get(Msg_427).text)
            self.get(CheckKick_216).set_value(self.get(StringParser_43).get_element(-1 + 1))
            self.get(CheckDaMap_176).set_value(self.get(StringParser_43).get_element(-1 + 2))
        self.set_event_id(300)
        if (self.groups['Client main'] and
        os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(CheckKick_216).text+'.sdo')):
            self.groups['Map change'] = True
            ClearScreen((0, 0, 0))
            self.add_hud_line('Change map to '+self.get(CheckKick_216).text)
            self.get(ChosedMap_125).set_value(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(CheckKick_216).text+'.sdo')
            self.get(ChosedMapWithoutPath_126).set_value(self.get(CheckKick_216).text)
            self.get(SpawnArea_192).destroy()
            self.get(qualifier_1).destroy()
            self.get(qualifier_2).destroy()
            self.get(qualifier_3).destroy()
            self.get(AmmoPack_208).destroy()
            self.get(ChangeMap_217).set_visible(True)
            self.get(ChangeMap_217).set_value('Game starts in a few seconds')
            self.get(Respawn_201).set_value(20)
            self.get(FlashTime_381).set_value(0)
            self.groups['Load Map'] = True
        self.set_event_id(301)
        if (self.groups['Client main'] and
        negate(os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(CheckKick_216).text+'.sdo'))):
            self.get(ErrorMsg_244).set_value('Map '+self.get(CheckKick_216).text+' not found')
            self.groups['Disconnect'] = True
        pass
    
    def function_222(self, int_arg = None):
        self.set_event_id(296)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(297)
        if self.groups['Client main']:
            self.get(ChangeMap_217).set_value(self.get(Msg_427).text)
            self.get(MsgCounter_332).set_value(10)
            self.groups['Msg'] = True
            self.get(ChangeMap_217).set_visible(True)
            chatting = self.get_by_id(Chatting_355, 
                self.get(NotID_430).get_value())
            chatting.values[1] = 0
        pass
    
    def function_fire(self, int_arg = None):
        self.set_event_id(597)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(8)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(8)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
        self.set_event_id(598)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(4)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(4)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
        self.set_event_id(599)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(0)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(0)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
        self.set_event_id(600)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(28)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(28)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
        self.set_event_id(601)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(24)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(24)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
        self.set_event_id(602)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(20)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(20)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
        self.set_event_id(603)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(16)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(16)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
        self.set_event_id(604)
        if (self.groups['Game'] and
        select(self.get(P1_452).values.get(2, 0) == int_arg)):
            self.create_object(Active17_451, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Active17_451'}
            self.get(Active17_451).set_direction(12)
            self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
            self.get(Active17_451).values[1] = self.get(P1_452).values[1]
            self.create_object(FlameDmg_456, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'FlameDmg_456'}
            self.get(Active17_451).values[4] = 'self.get(FlameDmg_456).FixedValue'
            self.get(FlameDmg_456).set_direction(12)
            self.get(FlameDmg_456).values[1] = self.get(Active17_451).values[1]
            self.get(FlameDmg_456).set_visible(False)
            self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
            self.get(P1_452).values[20] -= 1
            self.get(P1_452).values[22] = 20
        pass
    
    def function_shc(self, int_arg = None):
        self.set_event_id(808)
        if (self.groups['Client'] and
        False):
            self.create_object(Cp2_435, 116, 767) # {'y': 767, 'x': 116, 'create_object': 'Cp2_435'}
            self.get(Cp2c_436).set_value(0)
            self.groups['Speed Hack'] = True
        pass
    
    def function_221(self, int_arg = None):
        self.set_event_id(364)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(365)
        if (self.groups['Both'] and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Chatting_355).values[1] = 0
        self.set_event_id(366)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(18, 0) == self.get(Fusssoldat_193).values[8]) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat_193).values[22] = 0
            self.add_hud_line(self.get(NameTag2_429).get_text()+'(Team): '+self.get(Msg_427).text)
            self.get(DurchlaufChat_245).set_value(0)
        pass
    
    def function_208(self, int_arg = None):
        self.set_event_id(327)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(328)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text)%100 == 0):
            self.create_object(Active8_196, 121, -61) # {'y': -61, 'x': 121, 'create_object': 'Active8_196'}
            self.get(Active8_196).set_position(x = (to_number(self.get(Msg_427).text)%100000)/100)
            self.get(Active8_196).set_position(y = to_number(self.get(Msg_427).text)/100000)
            self.create_object(HitBack_198, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Active8_196).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
            return
        self.set_event_id(329)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text) > 9999 and
        to_number(self.get(Msg_427).text)%100 != 0):
            self.create_object(Active8_196, 121, -61) # {'y': -61, 'x': 121, 'create_object': 'Active8_196'}
            self.get(Active8_196).set_position(x = (to_number(self.get(Msg_427).text)%100000)/100)
            self.get(Active8_196).set_position(y = to_number(self.get(Msg_427).text)/100000)
            self.get(Fusssoldat2_194).LookAt({'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)'})
            self.create_object(HitBack_198, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'HitBack_198'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.create_object(Splitter_202, self.get(Active8_196).x + 0, self.get(Active8_196).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active8_196)', 'create_object': 'Splitter_202'}
            self.get(Splitter_202).values[9] = self.get(Splitter_202).y*1000-2000
            self.get(Active8_196).destroy()
            self.get(Splitter_202).values[0] = -6+randrange(6)
            self.get(Splitter_202).values[1] = randrange(7)-3
        self.set_event_id(330)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        to_number(self.get(Msg_427).text) < 10000 and
        to_number(self.get(Msg_427).text)%100 != 0):
            self.get(Fusssoldat2_194).set_direction(to_number(self.get(Msg_427).text)/100)
        self.set_event_id(331)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 1 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('glock.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(332)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 2 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('ak47.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(333)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 3 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('m3.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(334)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 4 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('deagle.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(335)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 5 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            return
            SoundAutoPlay('sniper.wav')
        self.set_event_id(336)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 6 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('mp5.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(337)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 7 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('g3.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(338)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 8 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 2
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('sig.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(339)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 9 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('m4.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(340)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 10 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('galil.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(341)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 11 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            return
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('svd.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(342)
        if (self.groups['Both'] and
        to_number(self.get(Msg_427).text)%100 == 12 and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            self.get(Fusssoldat2_194).values[22] = 1
            SoundAutoPlay('sr60.wav')
        pass
    
    def function_220(self, int_arg = None):
        self.set_event_id(294)
        if self.groups['Client main']:
            self.values[3] = 0
            self.get(Msg_427).set_value('115'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        self.set_event_id(295)
        if (self.groups['Client main'] and
        select(self.get(Strafing_219).flags[9] == True)):
            self.get(Strafing_219).flags[9] = False
            self.groups['Custom Movement'] = True
            self.get(ChangeMap_217).set_value('')
            self.get(ChangeMap_217).set_visible(False)
        pass
    
    def function_201(self, int_arg = None):
        self.set_event_id(309)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(310)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10)):
            self.get(Strafing2_220).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Strafing2_220).values[23] = (to_number(self.get(Msg_427).text)%100000)/100
            self.get(Strafing2_220).values[24] = to_number(self.get(Msg_427).text)/100000
            self.get(Strafing2_220).values[17] = max(abs(self.get(Strafing2_220).values[23]-self.get(Strafing2_220).x), abs(self.get(Strafing2_220).values[24]-self.get(Strafing2_220).y))
            self.get(Strafing2_220).values[4] = 9
        self.set_event_id(311)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10) and
        select(self.get(Strafing2_220).direction_value == random.choice((0, 4, 28))) and
        select(self.get(Strafing2_220).values.get(17, 0) <= 100)):
            self.get(Strafing2_220).AddToAlterable(23, self.get(Strafing2_220).values[17])
        self.set_event_id(312)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10) and
        select(self.get(Strafing2_220).direction_value == random.choice((12, 16, 20))) and
        select(self.get(Strafing2_220).values.get(17, 0) <= 100)):
            self.get(Strafing2_220).values[23] -= self.get(Strafing2_220).values[17]
        self.set_event_id(313)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10) and
        select(self.get(Strafing2_220).direction_value == random.choice((20, 24, 28))) and
        select(self.get(Strafing2_220).values.get(17, 0) <= 100)):
            self.get(Strafing2_220).AddToAlterable(24, self.get(Strafing2_220).values[17])
        self.set_event_id(314)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10) and
        select(self.get(Strafing2_220).direction_value == random.choice((4, 8, 12))) and
        select(self.get(Strafing2_220).values.get(17, 0) <= 100)):
            self.get(Strafing2_220).values[24] -= self.get(Strafing2_220).values[17]
        self.set_event_id(315)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(17, 0) > 100) and
        select(self.get(Respawn_201).get_value() <= 10)):
            self.get(Strafing2_220).set_position(x = self.get(Strafing2_220).values[23])
            self.get(Strafing2_220).set_position(y = self.get(Strafing2_220).values[24])
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Strafing2_220).values[4] = 9
        pass
    
    def function_200(self, int_arg = None):
        self.set_event_id(306)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(307)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Respawn_201).get_value() > 10)):
            self.get(Strafing2_220).values[4] = 0
            self.get(Fusssoldat2_194).values[25] = 1
            self.get(Strafing2_220).values[25] = 1
            self.get(Fusssoldat2_194).values[17] = to_number(self.get(Msg_427).text)/1000000
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Fusssoldat2_194).values[15] = 0
        self.set_event_id(308)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Respawn_201).get_value() <= 10)):
            self.get(Strafing2_220).values[4] = 0
            self.get(Strafing2_220).set_position(x = to_number(self.get(Msg_427).text)%1000)
            self.get(Strafing2_220).set_position(y = (to_number(self.get(Msg_427).text)%1000000)/1000)
            self.get(Fusssoldat2_194).values[25] = 1
            self.get(Strafing2_220).values[25] = 1
            self.get(Fusssoldat2_194).values[17] = to_number(self.get(Msg_427).text)/1000000
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
            self.get(Fusssoldat2_194).values[15] = 0
        pass
    
    def function_203(self, int_arg = None):
        self.set_event_id(319)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(320)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10)):
            self.get(Strafing2_220).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Strafing2_220).values[4] = 9
            self.get(Strafing2_220).movement.set_speed(9)
            self.get(Strafing2_220).movement.start()
        pass
    
    def function_202(self, int_arg = None):
        self.set_event_id(316)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(317)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10)):
            self.get(Strafing2_220).values[4] = 0
            self.get(Strafing2_220).movement.stop()
            self.get(Strafing2_220).values[23] = to_number(self.get(Msg_427).text)%1000
            self.get(Strafing2_220).values[24] = to_number(self.get(Msg_427).text)/1000
            self.get(Strafing2_220).values[17] = max(abs(self.get(Strafing2_220).values[23]-self.get(Strafing2_220).x), abs(self.get(Strafing2_220).values[24]-self.get(Strafing2_220).y))
        self.set_event_id(318)
        if (self.groups['Both'] and
        select(self.get(Strafing2_220).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Strafing2_220).values.get(25, 0) == 1) and
        select(self.get(Strafing2_220).values.get(17, 0) > 100) and
        select(self.get(Respawn_201).get_value() <= 10)):
            self.get(Strafing2_220).set_position(x = self.get(Strafing2_220).values[23])
            self.get(Strafing2_220).set_position(y = self.get(Strafing2_220).values[24])
            self.get(Strafing2_220).values[23] = 0
            self.get(Strafing2_220).values[24] = 0
        pass
    
    def function_205(self, int_arg = None):
        self.set_event_id(323)
        if (self.groups['Both'] and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Chatting_355).values[1] = 0
        pass
    
    def function_204(self, int_arg = None):
        self.set_event_id(321)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(322)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Respawn_201).get_value() <= 10)):
            self.get(Fusssoldat2_194).set_direction(to_number(self.get(Msg_427).text))
        pass
    
    def function_rec_n(self, int_arg = None):
        self.set_event_id(57)
        if (self.groups['Server main'] and
        left_string(self.get(Msg_427).text, 2) == '00' and
        False):
            self.get(Moo_181).set_property('timeout', '0')
            getattr(self, "function_" + left_string(self.get(Msg_427).text, 3))()
        self.set_event_id(58)
        if (self.groups['Server main'] and
        left_string(self.get(Msg_427).text, 2) != '00'):
            self.get(Msg_427).set_value(decrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        self.set_event_id(59)
        if (self.groups['Server main'] and
        left_string(self.get(Msg_427).text, 1) == '1'):
            self.get(Moo_181).set_property('timeout', '0')
            self.get(NotID_430).set_value(to_number(mid_string(self.get(Msg_427).text, 3, 2)))
            getattr(self, "function_" + left_string(self.get(Msg_427).text, 3))()
        self.set_event_id(60)
        if (self.groups['Server main'] and
        left_string(self.get(Msg_427).text, 1) == '2'):
            self.get(Moo_181).set_property('timeout', '0')
            self.get(NotID_430).set_value(to_number(mid_string(self.get(Msg_427).text, 3, 2)))
            self.get(Csm_432).set_value(to_number(right_string(self.get(Msg_427).text, 1)))
            self.function_csm()
            self.function_sendall()
            getattr(self, "function_" + left_string(self.get(Msg_427).text, 3))()
        pass
    
    def function_206(self, int_arg = None):
        self.set_event_id(324)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
            self.get(DurchlaufChat_245).set_value(0)
        self.set_event_id(325)
        if (self.groups['Both'] and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(NameTag2_429).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat_193).values[22] = 0
            self.add_hud_line(self.get(NameTag2_429).get_text()+': '+self.get(Msg_427).text)
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Chatting_355).values[1] = 0
        pass
    
    def function_209(self, int_arg = None):
        self.set_event_id(343)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(344)
        if (self.groups['Both'] and
        self.get(Msg_427).text == '1' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('reload.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        self.set_event_id(345)
        if (self.groups['Both'] and
        self.get(Msg_427).text == '2' and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
            SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
            SoundAutoPlayPosition('clipin.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        pass
    
    def function_rec_join(self, int_arg = None):
        self.set_event_id(52)
        if (self.groups['Server main'] and
        left_string(self.get(Msg2_449).text, 2) == '00'):
            self.get(Moo2_447).set_property('timeout', '0')
            getattr(self, "function_" + left_string(self.get(Msg2_449).text, 3))()
        pass
    
    def function_gas(self, int_arg = None):
        self.set_event_id(581)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(8)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        self.set_event_id(582)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(4)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        self.set_event_id(583)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(0)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        self.set_event_id(584)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(28)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        self.set_event_id(585)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(24)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        self.set_event_id(586)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(20)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        self.set_event_id(587)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(16)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        self.set_event_id(588)
        if (self.groups['Game'] and
        select(self.get(Nade_458).values.get(0, 0) >= 100) and
        select(self.get(Nade_458).values.get(1, 0) == 1)):
            self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
            self.get(Gaswolke_215).set_direction(12)
            self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
        pass
    
    def function_pleft(self, int_arg = None):
        self.set_event_id(69)
        if (self.groups['Server main'] and
        select(self.get(NameTag2_429).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        select(self.get(NameTag3_433).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.add_hud_line(self.get(NameTag2_429).get_text()+' left the game')
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Players_317).subtract_value(1)
            self.get(NameTag2_429).destroy()
            self.get(NameTag3_433).destroy()
            self.get(Fusssoldat_193).flags[24] = True
        self.set_event_id(70)
        if (self.groups['Server main'] and
        select(self.get(Head_441).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Head_441).destroy()
        self.set_event_id(71)
        if (self.groups['Server main'] and
        select(self.get(Chatting_355).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Chatting_355).destroy()
        self.set_event_id(72)
        if (self.groups['Server main'] and
        select(self.get(Gaswolke_215).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Gaswolke_215).destroy()
        self.set_event_id(73)
        if (self.groups['Server main'] and
        select(self.get(Active17_451).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Active17_451).destroy()
        self.set_event_id(74)
        if (self.groups['Server main'] and
        select(self.get(P1_452).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(P1_452).destroy()
        self.set_event_id(75)
        if (self.groups['Server main'] and
        select(self.get(FlameDmg_456).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(FlameDmg_456).destroy()
        self.set_event_id(76)
        if (self.groups['Server main'] and
        select(self.get(BigflameDmg_457).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(BigflameDmg_457).destroy()
        self.set_event_id(77)
        if (self.groups['Server main'] and
        select(self.get(Nade_458).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Nade_458).destroy()
        self.set_event_id(78)
        if (self.groups['Server main'] and
        select(self.get(Molotov_450).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Molotov_450).destroy()
        self.set_event_id(79)
        if (self.groups['Server main'] and
        select(self.get(C4_374).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Reclist_426).delete_line(self.get(Reclist_426).find_exact(str(self.get(C4_374).x)+','+str(self.get(C4_374).y), 1))
            self.get(C4_374).destroy()
        self.set_event_id(80)
        if (self.groups['Server main'] and
        select(self.get(Exp_247).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Exp_247).destroy()
        self.set_event_id(81)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        select(self.get(PlShadow2_383).PickRandom()) and
        self.get(Msg_427).text != ''):
            self.get(PlShadow2_383).destroy()
        self.set_event_id(82)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Fusssoldat2_194).destroy()
        self.set_event_id(83)
        if (self.groups['Server main'] and
        select(self.get(Strafing2_220).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != ''):
            self.get(Strafing2_220).destroy()
        self.set_event_id(84)
        if (self.groups['Server main'] and
        self.get(Msg_427).text != ''):
            self.groups['User left'] = True
            self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
            self.get(IdAllocation_425).set_value(2)
            for loop_index in xrange(98):
                if self.loop_alloid(loop_index) == False: break
            self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+','+self.get(Version_26).text+','+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
        pass
    
    def function_120(self, int_arg = None):
        self.set_event_id(158)
        if self.groups['Server main']:
            self.get(Msg_427).set_value('224'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
            self.get(Msg_427).set_value(self.get(Msg_427).text+immediate_compare(self.get(GlobalValues_165).values[0], '=', 0, 'No map cycle', str(self.get(GlobalValues_165).values[1]/60)+':'+immediate_compare((self.get(GlobalValues_165).values[1]%60), '<', 10, '0'+str(self.get(GlobalValues_165).values[1]%60), str(self.get(GlobalValues_165).values[1]%60))+' min left')+str(self.get(Csm_432).get_value()))
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        pass
    
    def function_121(self, int_arg = None):
        self.set_event_id(159)
        if self.groups['Server main']:
            self.get(Msg_427).set_value('224'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
            self.get(Msg_427).set_value(self.get(Msg_427).text+immediate_compare(self.get(GlobalValues_165).values[0], '=', 0, 'No map cycle', immediate_compare(self.get(GlobalValues_165).values[2], '<', 'self.get(Mapcycle_417).ListGetLineCount', 'Next map is '+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2]+1), 'Next map is '+self.get(Mapcycle_417).get_line(2)))+str(self.get(Csm_432).get_value()))
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        pass
    
    def function_001(self, int_arg = None):
        self.set_event_id(86)
        if (self.groups['Server main'] and
        select(self.get(GlobalValues_165).values.get(3, 0) == 0)):
            self.get(Moo2_447).send_line(encrypt_string('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9', 'n'))
        self.set_event_id(87)
        if (self.groups['Server main'] and
        select(self.get(GlobalValues_165).values.get(3, 0) == 1)):
            self.get(Moo2_447).send_line(encrypt_string('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9', 'y'))
        pass
    
    def function_123(self, int_arg = None):
        self.set_event_id(93)
        if self.groups['Server main']:
            self.get(Msg_427).set_value('10501'+str('self.get(Strafing_219).GetDirection')+','+str('self.get(Strafing_219).Speed')+','+str(self.get(Strafing_219).x)+','+str(self.get(Strafing_219).y)+','+str(self.get(Fusssoldat_193).values[14])+','+str(self.get(Ping_233).get_value())+','+str(self.get(Deaths_210).get_value())+','+str(self.get(Fusssoldat_193).values[8])+','+str(self.get(ChattingPlayer_356).values[1])+','+str(self.get(Frags_209).get_value())+','+self.get(GlobalName_6).text)
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        self.set_event_id(94)
        if self.groups['Server main']:
            self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
        self.set_event_id(95)
        if self.groups['Server main']:
            for loop_index in xrange('self.get(Fusssoldat2_194).ObjectCount'):
                if self.loop_pinfo(loop_index) == False: break
            self.get(Moo_181).set_property('snd', self.get(Moo_181).get_property('sndnew'))
        pass
    
    def function_241(self, int_arg = None):
        self.set_event_id(371)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(372)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.create_object(Nade2_459, -34, 174) # {'y': 174, 'x': -34, 'create_object': 'Nade2_459'}
            self.get(Nade2_459).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Nade2_459).set_position(x = (to_number(self.get(Msg_427).text)%1000000)/1000)
            self.get(Nade2_459).set_position(y = to_number(self.get(Msg_427).text)/1000000)
            self.get(Nade2_459).movement.set_speed((to_number(self.get(Msg_427).text)%1000)/100+10)
            self.get(Fusssoldat2_194).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Nade2_459).values[23] = 2
        pass
    
    def function_240(self, int_arg = None):
        self.set_event_id(368)
        if self.groups['Both']:
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(Msg_427).set_value(left_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-1))
        self.set_event_id(369)
        if (self.groups['Both'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Fusssoldat2_194).set_direction(to_number(self.get(Msg_427).text)%100)
        self.set_event_id(370)
        if self.groups['Both']:
            self.create_object(Molotov_450, 21, -62) # {'y': -62, 'x': 21, 'create_object': 'Molotov_450'}
            self.get(Molotov_450).values[2] = self.get(NotID_430).get_value()
            self.get(Molotov_450).values[1] = 1
            self.get(Molotov_450).set_direction(to_number(self.get(Msg_427).text)%100)
            self.get(Molotov_450).set_position(x = (to_number(self.get(Msg_427).text)%1000000)/1000)
            self.get(Molotov_450).set_position(y = to_number(self.get(Msg_427).text)/1000000)
            self.get(Molotov_450).SetSpeed((to_number(self.get(Msg_427).text)%1000)/100+5)
            self.get(Molotov_450).values[9] = 11110000
        pass
    
    def function_102(self, int_arg = None):
        self.set_event_id(187)
        if self.groups['Client main']:
            self.create_object(Fusssoldat2_194, 195, -54) # {'y': -54, 'x': 195, 'create_object': 'Fusssoldat2_194'}
            self.get(Fusssoldat2_194).values[0] = to_number(mid_string(self.get(Msg_427).text, 3, 2))
            self.create_object(NameTag2_429, 528, 633) # {'y': 633, 'x': 528, 'create_object': 'NameTag2_429'}
            self.create_object(Strafing2_220, 132, -59) # {'y': -59, 'x': 132, 'create_object': 'Strafing2_220'}
            self.get(Strafing2_220).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Strafing2_220).set_visible(False)
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(Fusssoldat2_194).values[24] = 100
            self.get(NameTag2_429).set_text(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(NameTag2_429).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Players_317).add_value(1)
            self.create_object(Chatting_355, 189, 647) # {'y': 647, 'x': 189, 'create_object': 'Chatting_355'}
            self.get(Chatting_355).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Chatting_355).values[9] = 10000001
            self.create_object(PlShadow2_383, 319, 664) # {'y': 664, 'x': 319, 'create_object': 'PlShadow2_383'}
            self.get(Fusssoldat2_194).values[12] = self.get(Fusssoldat2_194).values[0]
            self.get(Strafing2_220).values[12] = self.get(Fusssoldat2_194).values[0]
            self.create_object(Head_441, 67, -33) # {'y': -33, 'x': 67, 'create_object': 'Head_441'}
            self.get(Head_441).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Head_441).set_visible(False)
            self.create_object(NameTag3_433, -270, 381) # {'y': 381, 'x': -270, 'create_object': 'NameTag3_433'}
            self.get(NameTag2_429).values[9] = 9999997
            self.get(NameTag3_433).values[9] = 9999996
            self.get(NameTag3_433).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(NameTag3_433).set_text(self.get(NameTag2_429).get_text())
        self.set_event_id(188)
        if (self.groups['Client main'] and
        self.get_global_value(6) == 1):
            self.get(PlShadow2_383).set_effect('None')
        self.set_event_id(189)
        if (self.groups['Client main'] and
        self.get_global_value(6) >= 2):
            self.get(PlShadow2_383).destroy()
        pass
    
    def function_103(self, int_arg = None):
        self.set_event_id(190)
        if self.groups['Client main']:
            self.create_object(Fusssoldat2_194, 195, -54) # {'y': -54, 'x': 195, 'create_object': 'Fusssoldat2_194'}
            self.get(Fusssoldat2_194).values[0] = self.get(NotID_430).get_value()
            self.create_object(NameTag2_429, 528, 633) # {'y': 633, 'x': 528, 'create_object': 'NameTag2_429'}
            self.create_object(Strafing2_220, 132, -59) # {'y': -59, 'x': 132, 'create_object': 'Strafing2_220'}
            self.get(Strafing2_220).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Strafing2_220).set_visible(False)
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(Fusssoldat2_194).values[24] = 100
            self.get(NameTag2_429).set_text(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            self.get(NameTag2_429).values[0] = self.get(Fusssoldat2_194).values[0]
            self.add_hud_line(self.get(NameTag2_429).get_text()+' joined the game')
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Players_317).add_value(1)
            self.create_object(Chatting_355, 189, 647) # {'y': 647, 'x': 189, 'create_object': 'Chatting_355'}
            self.get(Chatting_355).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Chatting_355).values[9] = 10000001
            self.create_object(PlShadow2_383, 319, 664) # {'y': 664, 'x': 319, 'create_object': 'PlShadow2_383'}
            self.get(Fusssoldat2_194).values[12] = self.get(Fusssoldat2_194).values[0]
            self.get(Strafing2_220).values[12] = self.get(Fusssoldat2_194).values[0]
            self.create_object(Head_441, 67, -33) # {'y': -33, 'x': 67, 'create_object': 'Head_441'}
            self.get(Head_441).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Head_441).set_visible(False)
            self.create_object(NameTag3_433, -270, 381) # {'y': 381, 'x': -270, 'create_object': 'NameTag3_433'}
            self.get(NameTag2_429).values[9] = 9999997
            self.get(NameTag3_433).values[9] = 9999996
            self.get(NameTag3_433).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(NameTag3_433).set_text(self.get(NameTag2_429).get_text())
        self.set_event_id(191)
        if (self.groups['Client main'] and
        self.get_global_value(6) == 1):
            self.get(PlShadow2_383).set_effect('None')
        self.set_event_id(192)
        if (self.groups['Client main'] and
        self.get_global_value(6) >= 2):
            self.get(PlShadow2_383).destroy()
        pass
    
    def function_225(self, int_arg = None):
        self.set_event_id(367)
        if (self.groups['Both'] and
        select(self.get(Chatting_355).values.get(0, 0) == self.get(NotID_430).get_value())):
            self.get(Chatting_355).values[1] = 1
        pass
    
    def function_101(self, int_arg = None):
        self.set_event_id(97)
        if (self.groups['Server main'] and
        self.get(Players_317).get_value() >= self.get(MaxPlayer_102).get_value()):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '106'))
            return
        self.set_event_id(98)
        if (self.groups['Server main'] and
        False):
            self.get(NameTag2_429).SpreadValue(21, 0, 0)
        self.set_event_id(99)
        if (self.groups['Server main'] and
        False):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '10201'+self.get(GlobalName_6).text))
            for loop_index in xrange('self.get(NameTag2_429).ObjectCount'):
                if self.loop_userishere(loop_index) == False: break
        self.set_event_id(101)
        if self.groups['Server main']:
            self.create_object(Fusssoldat2_194, 195, -54) # {'y': -54, 'x': 195, 'create_object': 'Fusssoldat2_194'}
            self.get(Fusssoldat2_194).values[0] = self.get(IdAllocation_425).get_value()
            self.create_object(NameTag2_429, 528, 633) # {'y': 633, 'x': 528, 'create_object': 'NameTag2_429'}
            self.create_object(Strafing2_220, 132, -59) # {'y': -59, 'x': 132, 'create_object': 'Strafing2_220'}
            self.get(Strafing2_220).values[0] = self.get(IdAllocation_425).get_value()
            self.get(Strafing2_220).set_visible(False)
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(Fusssoldat2_194).values[24] = 100
            self.get(NameTag2_429).set_text(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-3))
            self.get(NameTag2_429).values[0] = self.get(IdAllocation_425).get_value()
            self.add_hud_line(self.get(NameTag2_429).get_text()+' joined the game')
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Players_317).add_value(1)
            self.create_object(Chatting_355, 189, 647) # {'y': 647, 'x': 189, 'create_object': 'Chatting_355'}
            self.get(Chatting_355).values[0] = self.get(IdAllocation_425).get_value()
            self.get(Chatting_355).values[9] = 10000001
            self.create_object(PlShadow2_383, 319, 664) # {'y': 664, 'x': 319, 'create_object': 'PlShadow2_383'}
            self.get(Fusssoldat2_194).values[12] = self.get(IdAllocation_425).get_value()
            self.get(Strafing2_220).values[12] = self.get(IdAllocation_425).get_value()
            self.get(Fusssoldat2_194).values[16] = 8
            self.create_object(Head_441, 67, -33) # {'y': -33, 'x': 67, 'create_object': 'Head_441'}
            self.get(Head_441).values[0] = self.get(IdAllocation_425).get_value()
            self.get(Head_441).set_visible(False)
            self.create_object(NameTag3_433, -270, 381) # {'y': 381, 'x': -270, 'create_object': 'NameTag3_433'}
            self.get(NameTag2_429).values[9] = 9999997
            self.get(NameTag3_433).values[9] = 9999996
            self.get(NameTag3_433).values[0] = self.get(IdAllocation_425).get_value()
            self.get(NameTag3_433).set_text(self.get(NameTag2_429).get_text())
            self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+','+self.get(Version_26).text+','+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
            self.get(Moo_181).set_property('sndnew', str(self.get(IdAllocation_425).get_value()))
            print 'send2'
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '101'+immediate_compare(self.get(IdAllocation_425).get_value(), '<', 10, '0'+str(self.get(IdAllocation_425).get_value()), str(self.get(IdAllocation_425).get_value()))))
            self.get(NotID_430).set_value(self.get(IdAllocation_425).get_value())
            self.get(Msg_427).set_value('103'+immediate_compare(self.get(IdAllocation_425).get_value(), '<', 10, '0'+str(self.get(IdAllocation_425).get_value()), str(self.get(IdAllocation_425).get_value()))+self.get(NameTag2_429).get_text())
            self.function_sendall()
        self.set_event_id(102)
        if (self.groups['Server main'] and
        self.get_global_value(6) == 1):
            self.get(PlShadow2_383).set_effect('None')
        self.set_event_id(103)
        if (self.groups['Server main'] and
        self.get_global_value(6) >= 2):
            self.get(PlShadow2_383).destroy()
        self.set_event_id(104)
        if (self.groups['Server main'] and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '114'+str(self.get(ScorePolice_368).get_value())+','+str(self.get(ScoreTerror_369).get_value())))
        self.set_event_id(105)
        if self.groups['Server main']:
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '116'+self.get(ChosedMapWithoutPath_126).text))
        self.set_event_id(106)
        if (self.groups['Server main'] and
        False):
            self.get(AmmoPack_208).SpreadValue(21, 0, 0)
        self.set_event_id(107)
        if (self.groups['Server main'] and
        False):
            for loop_index in xrange(len(self.get(AmmoPack_208), True)):
                if self.loop_crates(loop_index) == False: break
        self.set_event_id(109)
        if self.groups['Server main']:
            self.get(C4_374).SpreadValue(21, 0, 0)
        self.set_event_id(110)
        if self.groups['Server main']:
            for loop_index in xrange('self.get(C4_374).ObjectCount'):
                if self.loop_c4s(loop_index) == False: break
        self.set_event_id(112)
        if self.groups['Server main']:
            for loop_index in xrange('self.get(Reclist_426).ListGetLineCount'):
                if self.loop_c4dmg(loop_index) == False: break
        self.set_event_id(114)
        if self.groups['Server main']:
            self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
            self.get(IdAllocation_425).set_value(2)
            for loop_index in xrange(98):
                if self.loop_alloid(loop_index) == False: break
        self.set_event_id(183)
        if self.groups['Client main']:
            self.get(VisibleId_424).set_value(to_number(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-3)))
            self.values[3] = 0
        self.set_event_id(184)
        if self.groups['Client main']:
            self.get(Fusssoldat_193).values[0] = self.get(VisibleId_424).get_value()
            self.add_hud_line(self.get(GlobalName_6).text+' joined the game')
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(ChangeMap_217).set_value(self.get(MessageOfDay_58).text)
            self.get(ChangeMap_217).set_visible(True)
            self.values[3] = 0
            self.groups['Crates'] = True
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '123'))
        self.set_event_id(185)
        if (self.groups['Client main'] and
        select(self.get(Mode_344).get_value() == 0)):
            self.get(String2_200).set_visible(True)
            self.get(Respawn_201).set_visible(True)
        self.set_event_id(186)
        if (self.groups['Client main'] and
        select(self.get(Mode_344).get_value() == 1)):
            self.get(Respawn_201).set_value(9)
            self.get(Police_342).set_visible(True)
            self.get(Terror_343).set_visible(True)
            self.groups['Join Team'] = True
        pass
    
    def function_106(self, int_arg = None):
        self.set_event_id(213)
        if self.groups['Client main']:
            self.get(ServerError_60).set_value('Server is full')
            self.set_frame(4)
        pass
    
    def function_107(self, int_arg = None):
        self.set_event_id(214)
        if self.groups['Client main']:
            self.get(ServerError_60).set_value('Sending error!')
            self.set_frame(4)
        pass
    
    def function_104(self, int_arg = None):
        self.set_event_id(193)
        if self.groups['Client main']:
            self.get(Msg_427).set_value(mid_string(self.get(Msg_427).text, 3, 2))
        self.set_event_id(194)
        if (self.groups['Client main'] and
        select(self.get(NameTag2_429).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        select(self.get(NameTag3_433).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.add_hud_line(self.get(NameTag2_429).get_text()+' left the game')
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Players_317).subtract_value(1)
            self.get(NameTag2_429).destroy()
            self.get(NameTag3_433).destroy()
        self.set_event_id(195)
        if (self.groups['Client main'] and
        select(self.get(Head_441).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Head_441).destroy()
        self.set_event_id(196)
        if (self.groups['Client main'] and
        select(self.get(Chatting_355).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Chatting_355).destroy()
        self.set_event_id(197)
        if (self.groups['Client main'] and
        select(self.get(Gaswolke_215).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Gaswolke_215).destroy()
        self.set_event_id(198)
        if (self.groups['Client main'] and
        select(self.get(Active17_451).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Active17_451).destroy()
        self.set_event_id(199)
        if (self.groups['Client main'] and
        select(self.get(P1_452).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(P1_452).destroy()
        self.set_event_id(200)
        if (self.groups['Client main'] and
        select(self.get(FlameDmg_456).values.get(1, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(FlameDmg_456).destroy()
        self.set_event_id(201)
        if (self.groups['Client main'] and
        select(self.get(BigflameDmg_457).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(BigflameDmg_457).destroy()
        self.set_event_id(202)
        if (self.groups['Client main'] and
        select(self.get(Nade_458).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Nade_458).destroy()
        self.set_event_id(203)
        if (self.groups['Client main'] and
        select(self.get(Molotov_450).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Molotov_450).destroy()
        self.set_event_id(204)
        if (self.groups['Client main'] and
        select(self.get(C4_374).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(C4_374).destroy()
        self.set_event_id(205)
        if (self.groups['Client main'] and
        select(self.get(Exp_247).values.get(2, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Exp_247).destroy()
        self.set_event_id(206)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        select(self.get(PlShadow2_383).PickRandom()) and
        self.get(Msg_427).text != '0'):
            self.get(PlShadow2_383).destroy()
        self.set_event_id(207)
        if (self.groups['Client main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Fusssoldat2_194).destroy()
        self.set_event_id(208)
        if (self.groups['Client main'] and
        select(self.get(Strafing2_220).values.get(0, 0) == to_number(self.get(Msg_427).text)) and
        self.get(Msg_427).text != '0'):
            self.get(Strafing2_220).destroy()
        pass
    
    def function_105(self, int_arg = None):
        self.set_event_id(119)
        if self.groups['Server main']:
            self.get(Moo_181).SockSelectSockWithProperty('snd', str(to_number(mid_string(self.get(Msg_427).text, 3, 2))))
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '105'+right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5)))
        self.set_event_id(209)
        if self.groups['Client main']:
            self.get(StringParser_43).set_value(self.get(Msg_427).text)
            self.create_object(Fusssoldat2_194, 195, -54) # {'y': -54, 'x': 195, 'create_object': 'Fusssoldat2_194'}
            self.get(Fusssoldat2_194).values[0] = to_number(mid_string(self.get(Msg_427).text, 3, 2))
            self.create_object(NameTag2_429, 528, 633) # {'y': 633, 'x': 528, 'create_object': 'NameTag2_429'}
            self.create_object(Strafing2_220, 132, -59) # {'y': -59, 'x': 132, 'create_object': 'Strafing2_220'}
            self.get(Strafing2_220).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Strafing2_220).set_visible(False)
            self.get(Fusssoldat2_194).values[5] = 1
            self.get(Fusssoldat2_194).values[24] = 100
            self.get(NameTag2_429).set_text(self.get(StringParser_43).get_element(-1 + 11))
            self.get(NameTag2_429).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Fusssoldat_193).values[22] = 0
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Players_317).add_value(1)
            self.create_object(Chatting_355, 189, 647) # {'y': 647, 'x': 189, 'create_object': 'Chatting_355'}
            self.get(Chatting_355).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Chatting_355).values[9] = 10000001
            self.create_object(PlShadow2_383, 319, 664) # {'y': 664, 'x': 319, 'create_object': 'PlShadow2_383'}
            self.get(Fusssoldat2_194).values[12] = self.get(Fusssoldat2_194).values[0]
            self.get(Strafing2_220).values[12] = self.get(Fusssoldat2_194).values[0]
            self.create_object(Head_441, 67, -33) # {'y': -33, 'x': 67, 'create_object': 'Head_441'}
            self.get(Head_441).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(Head_441).set_visible(False)
            self.create_object(NameTag3_433, -270, 381) # {'y': 381, 'x': -270, 'create_object': 'NameTag3_433'}
            self.get(NameTag2_429).values[9] = 9999997
            self.get(NameTag3_433).values[9] = 9999996
            self.get(NameTag3_433).values[0] = self.get(Fusssoldat2_194).values[0]
            self.get(NameTag3_433).set_text(self.get(NameTag2_429).get_text())
        self.set_event_id(210)
        if (self.groups['Client main'] and
        self.get_global_value(6) == 1):
            self.get(PlShadow2_383).set_effect('None')
        self.set_event_id(211)
        if (self.groups['Client main'] and
        self.get_global_value(6) >= 2):
            self.get(PlShadow2_383).destroy()
        self.set_event_id(212)
        if self.groups['Client main']:
            selected_id = self.get(NotID_430).get_value()
            movement = self.get_by_id(Strafing2_220, selected_id)
            character = self.get_by_id(Fusssoldat2_194, selected_id)
            chatting = self.get_by_id(Chatting_355, selected_id)
            self.get(Msg_427).set_value(right_string(self.get(Msg_427).text, len(self.get(Msg_427).text)-5))
            movement.set_direction(to_number(self.get(StringParser_43).get_element(-1 + 1)))
            movement.movement.set_speed(to_number(self.get(StringParser_43).get_element(-1 + 2)))
            movement.values[4] = to_number(self.get(StringParser_43).get_element(-1 + 2))
            movement.set_position(x = to_number(self.get(StringParser_43).get_element(-1 + 3)))
            movement.set_position(y = to_number(self.get(StringParser_43).get_element(-1 + 4)))
            character.values[25] = to_number(self.get(StringParser_43).get_element(-1 + 5))
            movement.values[25] = to_number(self.get(StringParser_43).get_element(-1 + 5))
            character.values[17] = to_number(self.get(StringParser_43).get_element(-1 + 6))
            character.values[8] = to_number(self.get(StringParser_43).get_element(-1 + 7))
            character.values[18] = to_number(self.get(StringParser_43).get_element(-1 + 8))
            chatting.values[1] = to_number(self.get(StringParser_43).get_element(-1 + 9))
            character.values[7] = to_number(self.get(StringParser_43).get_element(-1 + 10))
            movement.values[23] = 0
            movement.values[24] = 0
            character.values[15] = 0
        pass
    
    def function_csmup(self, int_arg = None):
        self.set_event_id(163)
        if self.groups['Server main']:
            self.get(Csm_432).set_value(immediate_compare((self.get(Csm_432).get_value()+1), '<', 10, (self.get(Csm_432).get_value()+1), 0))
        self.set_event_id(181)
        if self.groups['Client main']:
            self.get(Csm_432).set_value(immediate_compare((self.get(Csm_432).get_value()+1), '<', 10, (self.get(Csm_432).get_value()+1), 0))
        pass
    
    def get_by_id(self, klass, value):
        for item in self.get(klass, True):
            if item.values.get(0, None) == value:
                return item
        raise NotImplementedError('no id: %s %s' % (klass, value))

    def function_002(self, int_arg = None):
        self.set_event_id(88)
        if self.groups['Server main']:
            self.get(StringParser_43).set_value(self.get(Msg2_449).text)
        self.set_event_id(89)
        if (self.groups['Server main'] and
        self.get(StringParser_43).get_element(-1 + 3) != self.get(ChosedMapWithoutPath_126).text):
            self.get(Moo2_447).send_line(encrypt_string('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9', '2'))
        self.set_event_id(90)
        if (self.groups['Server main'] and
        to_number(self.get(StringParser_43).get_element(-1 + 2)) == 0 and
        self.get(StringParser_43).get_element(-1 + 3) == self.get(ChosedMapWithoutPath_126).text):
            self.get(Moo2_447).send_line(encrypt_string('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9', '3,'+str(self.get(LoadMap_259).get_count())))
        self.set_event_id(91)
        if (self.groups['Server main'] and
        to_number(self.get(StringParser_43).get_element(-1 + 2)) > 0 and
        self.get(StringParser_43).get_element(-1 + 3) == self.get(ChosedMapWithoutPath_126).text):
            self.get(Moo2_447).send_line(encrypt_string('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9', '3,'+self.get(LoadMap_259).get_line(to_number(self.get(StringParser_43).get_element(-1 + 2)))))
        pass
    
    def function_pleftsend(self, int_arg = None):
        self.set_event_id(68)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat_193).flags[24] == True)):
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('104'+immediate_compare(to_number(self.get(Msg_427).text), '<', 10, '0'+self.get(Msg_427).text, self.get(Msg_427).text))
            self.function_sendall()
        pass
    
    def function_108(self, int_arg = None):
        self.set_event_id(215)
        if self.groups['Client main']:
            self.get(ErrorMsg_244).set_value('Server closed')
            self.groups['Disconnect'] = True
        pass
    
    def function_000(self, int_arg = None):
        self.set_event_id(85)
        if self.groups['Server main']:
            self.get(Fusssoldat_193).flags[31] = False
            self.get(Checkip_395).set_value('self.get(Moo2_447).SockGetRemoteIP')
            self.get(StringParser_43).set_value(self.get(BanList_393).text)
            for loop_index in xrange(self.get(StringParser_43).get_count()):
                if self.loop_ban(loop_index) == False: break
            self.get(Moo2_447).send_line(encrypt_string('\xf88\xfa2J\xdb\xae\x91=\xd5.\x99\xb3_y\x7f/U%0C\xd9', immediate_compare(self.get(Fusssoldat_193).get_flag(31), '=', 1, '0', '1,'+self.get(Svrmotd_428).text+','+self.get(Sting_186).text)))
        pass
    
    def function_109(self, int_arg = None):
        self.set_event_id(120)
        if self.groups['Server main']:
            self.get(NotID_430).set_value(to_number(mid_string(self.get(Msg_427).text, 3, 2)))
            self.get(Csm_432).set_value(to_number(right_string(self.get(Msg_427).text, 1)))
            self.function_csm()
        self.set_event_id(121)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(24, 0) >= 60)):
            self.get(Fusssoldat2_194).values[24] = 100
        self.set_event_id(122)
        if (self.groups['Server main'] and
        select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(NotID_430).get_value()) and
        select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
        select(self.get(Fusssoldat2_194).values.get(24, 0) < 60)):
            self.get(Fusssoldat2_194).AddToAlterable(24, 40)
        pass
    
    def function_sendall(self, int_arg = None):
        self.set_event_id(65)
        if self.groups['Server main']:
            self.get(Temp_431).set_value(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
            for loop_index in xrange('self.get(Moo_181).SockCountSockets'-1):
                if self.loop_send(loop_index) == False: break
        self.set_event_id(182)
        if self.groups['Client main']:
            self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, self.get(Msg_427).text))
        pass
    
    def on_sock_receive(self, instance):
        print 'ON SOCK RECEIVE :))'
        if type(instance) == Moo2_447:
            self.set_event_id(51)
            if self.groups['Server main']:
                self.get(Msg2_449).set_value(self.get(Moo2_447).get_line())
                self.function_rec_join()
        if type(instance) == Moo_181:
            self.set_event_id(56)
            if self.groups['Server main']:
                self.get(Msg_427).set_value(self.get(Moo_181).get_line())
                self.function_rec_n()
        if type(instance) == Moo_181:
            self.set_event_id(177)
            if self.groups['Client main']:
                self.get(Msg_427).set_value(self.get(Moo_181).get_line())
                self.function_clrec()
        if type(instance) == MooSock_335:
            self.set_event_id(492)
            if self.groups['Add server']:
                self.get(MooSock_335).disconnect()
        pass
    
    def on_sock_connect(self, instance):
        if type(instance) == Moo_181:
            self.set_event_id(176)
            if self.groups['Client main']:
                self.get(Moo_181).send_line(encrypt_string(self.get(Sting_186).text, '101'+self.get(GlobalName_6).text))
                self.values[3] = 0
        if type(instance) == MooSock_335:
            self.set_event_id(490)
            if self.groups['Add server']:
                self.get(MooSock_335).send_text(self.get(Edit2_336).get_value())
                StartGlobalTimer(0)
        pass
    
    def on_sock_disconnect(self, instance):
        if type(instance) == Moo2_447:
            self.set_event_id(50)
            if self.groups['Server main']:
                self.get(Moo2_447).DeleteSocket()
        if type(instance) == Moo_181:
            self.set_event_id(53)
            if self.groups['Server main']:
                self.get(Fusssoldat_193).flags[24] = False
                self.get(Msg_427).set_value(self.get(Moo_181).get_property('sndnew'))
        if type(instance) == Moo_181:
            self.set_event_id(54)
            if self.groups['Server main']:
                self.get(Moo_181).DeleteSocket()
        if type(instance) == Moo_181:
            self.set_event_id(55)
            if self.groups['Server main']:
                self.get(Fusssoldat_193).flags[24] = False
                self.function_pleft()
                self.function_pleftsend()
        if type(instance) == Moo_181:
            self.set_event_id(180)
            if (self.groups['Client main'] and
            negate(self.groups['Disconnect']) and
            False):
                self.get(ErrorMsg_244).set_value('Connection lost to server')
                self.groups['Disconnect'] = True
        pass
    
    def on_sock_connection(self, instance):
        if type(instance) == Moo_181:
            self.set_event_id(41)
            if self.groups['Con']:
                self.get(Moo_181).accept()
                self.get(Moo_181).SelectSocket('self.get(Moo_181).SockCountSockets'-1)
                self.get(Moo_181).set_property('timeout', '0')
                self.get(Moo_181).set_property('snd', '0')
                self.get(Msg_427).set_value('self.get(Moo_181).SockGetRemoteIP')
        if type(instance) == Moo_181:
            self.set_event_id(42)
            if (self.groups['Con'] and
            False):
                self.get(Moo_181).accept()
                self.get(Moo_181).select_socket('self.get(Moo_181).SockCountSockets'-1)
                self.get(Moo_181).set_property('timeout', '0')
                self.get(Moo_181).set_property('snd', '0')
                self.get(Msg_427).set_value('self.get(Moo_181).SockGetRemoteIP')
                for loop_index in xrange(immediate_compare('self.get(Moo_181).SockCountSockets', '>', 1, 'self.get(Moo_181).SockCountSockets'-2, 0)):
                    if self.loop_doubleip(loop_index) == False: break
        if type(instance) == Moo2_447:
            self.set_event_id(45)
            if self.groups['Con']:
                self.get(Moo2_447).accept()
                self.get(Moo2_447).SelectSocket('self.get(Moo2_447).SockCountSockets'-1)
                self.get(Moo2_447).set_property('timeout', '0')
        pass
    
    def on_OnBackgroundCollision(self, instance):
        if type(instance) == AmmoPack_208:
            self.set_event_id(652)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnBackgroundCollision())):
                self.get(AmmoPack_208).destroy()
        if type(instance) == Active2_254:
            self.set_event_id(739)
            if (self.groups['Game'] and
            select(self.get(Active2_254).OnBackgroundCollision())):
                self.get(Active2_254).destroy()
        pass
    
    def on_PlayerKeyPressed(self, instance):
        self.set_event_id(667)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button2']) and
        self.players[0].lives == 1 and
        select(self.get(SecondWeapon_318).get_value() > 0) and
        select(self.get(Sleep_324).get_value() <= 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        negate(self.groups['Chat']) and
        negate(self.groups['Shop'])):
            self.players[0].lives = self.get(SecondWeapon_318).get_value()
            self.get(Ammo1_321).set_value(self.get(AmmoCurrent_311).get_value())
            self.get(AmmoCurrent_311).set_value(self.get(Ammo2_322).get_value())
            self.get(AmmoFull_312).set_value(self.get(Reload2_323).get_value())
            self.groups['Weapon Change Normal'] = True
            self.get(Active5_213).destroy()
            self.groups['Reload'] = False
            self.get(Accuracy_238).add_value(15)
            self.get(Sleep_324).set_value(5)
            SoundAutoPlay('collect.wav')
        self.set_event_id(668)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button2']) and
        self.players[0].lives == 8 and
        select(self.get(SecondWeapon_318).get_value() > 0) and
        select(self.get(Sleep_324).get_value() <= 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        negate(self.groups['Chat']) and
        negate(self.groups['Shop'])):
            self.players[0].lives = self.get(SecondWeapon_318).get_value()
            self.get(Ammo1_321).set_value(self.get(AmmoCurrent_311).get_value())
            self.get(AmmoCurrent_311).set_value(self.get(Ammo2_322).get_value())
            self.get(AmmoFull_312).set_value(self.get(Reload2_323).get_value())
            self.groups['Weapon Change Normal'] = True
            self.get(Active5_213).destroy()
            self.groups['Reload'] = False
            self.get(Accuracy_238).add_value(15)
            self.get(Sleep_324).set_value(5)
            SoundAutoPlay('collect.wav')
        self.set_event_id(669)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button2']) and
        self.players[0].lives != 8 and
        self.players[0].lives != 1 and
        select(self.get(Sleep_324).get_value() <= 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        negate(self.groups['Chat']) and
        negate(self.groups['Shop'])):
            self.players[0].lives = 1+7*self.get_global_value(9)
            self.get(Ammo2_322).set_value(self.get(AmmoCurrent_311).get_value())
            self.get(Reload2_323).set_value(self.get(AmmoFull_312).get_value())
            self.get(AmmoCurrent_311).set_value(self.get(Ammo1_321).get_value())
            self.get(AmmoFull_312).set_value(0)
            self.groups['Weapon Change Normal'] = True
            self.get(Active5_213).destroy()
            self.groups['Reload'] = False
            self.get(Accuracy_238).add_value(15)
            self.get(Sleep_324).set_value(5)
            SoundAutoPlay('collect.wav')
        self.set_event_id(670)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 1 and
        select(self.get(AmmoCurrent_311).get_value() < 15) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(671)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 2 and
        select(self.get(AmmoCurrent_311).get_value() < 30) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(672)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 3 and
        select(self.get(AmmoCurrent_311).get_value() < 8) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(673)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 4 and
        select(self.get(AmmoCurrent_311).get_value() < 7) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(674)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 6 and
        select(self.get(AmmoCurrent_311).get_value() < 30) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(675)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 7 and
        select(self.get(AmmoCurrent_311).get_value() < 20) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(676)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 8 and
        select(self.get(AmmoCurrent_311).get_value() < 13) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(677)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 9 and
        select(self.get(AmmoCurrent_311).get_value() < 30) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(678)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 10 and
        select(self.get(AmmoCurrent_311).get_value() < 25) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(679)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 11 and
        select(self.get(AmmoCurrent_311).get_value() < 10) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(680)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button1']) and
        self.players[0].lives == 12 and
        select(self.get(AmmoCurrent_311).get_value() < 4) and
        select(self.get(AmmoFull_312).get_value() > 0) and
        negate(self.groups['Chat'])):
            self.get(AmmoCurrent_311).set_value(0)
        self.set_event_id(799)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Button2']) and
        self.players[0].lives == 1 and
        select(self.get(SecondWeapon_318).get_value() > 0) and
        select(self.get(Sleep_324).get_value() <= 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        negate(self.groups['Chat']) and
        negate(self.groups['Shop'])):
            self.players[0].lives = self.get(SecondWeapon_318).get_value()
            self.get(Ammo1_321).set_value(self.get(AmmoCurrent_311).get_value())
            self.get(AmmoCurrent_311).set_value(self.get(Ammo2_322).get_value())
            self.get(AmmoFull_312).set_value(self.get(Reload2_323).get_value())
            self.groups['Weapon Change Normal'] = True
            self.get(Active5_213).destroy()
            self.groups['Reload'] = False
            self.get(Accuracy_238).add_value(15)
            self.get(Sleep_324).set_value(5)
            SoundAutoPlay('collect.wav')
        self.set_event_id(801)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Up']) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active9_222).values.get(7, 0) == 1)):
            self.get(Active9_222).values[7] = 2
        self.set_event_id(802)
        if (self.groups['Game'] and
        self.players[1].key_pressed(['Up']) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(Active9_222).values.get(7, 0) == 0)):
            self.get(Active9_222).values[7] = 1
            self.get(Oben_239).force_animation('User defined 1')
            self.get(Unten_240).force_animation('User defined 1')
            self.get(Rechts_241).force_animation('User defined 1')
            self.get(Links_242).force_animation('User defined 1')
        self.set_event_id(1064)
        if (self.groups['Custom Movement'] and
        self.players[0].key_pressed(['Up'])):
            self.get(Fusssoldat_193).flags[30] = True
            self.get(Fusssoldat_193).values[21] = 1
        self.set_event_id(1065)
        if (self.groups['Custom Movement'] and
        self.players[0].key_pressed(['Right'])):
            self.get(Fusssoldat_193).flags[30] = True
            self.get(Fusssoldat_193).values[21] = 1
        self.set_event_id(1066)
        if (self.groups['Custom Movement'] and
        self.players[0].key_pressed(['Down'])):
            self.get(Fusssoldat_193).flags[30] = True
            self.get(Fusssoldat_193).values[21] = 1
        self.set_event_id(1067)
        if (self.groups['Custom Movement'] and
        self.players[0].key_pressed(['Left'])):
            self.get(Fusssoldat_193).flags[30] = True
            self.get(Fusssoldat_193).values[21] = 1
        self.set_event_id(1156)
        if (self.groups['W1'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 1 and
        select(self.get(AmmoCurrent_311).get_value() == 0) and
        select(len(self.get(Active5_213, True)) == 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.get(ShotLatence_230).set_value(21)
            SoundAutoPlay('empty.wav')
        self.set_event_id(1157)
        if (self.groups['W1'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 1 and
        select(self.get(AmmoCurrent_311).get_value() >= 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(len(self.get(Active7_195, True)) == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
            self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
            self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
            self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
            self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
            self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 12, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 12, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[23] = self.get(Active7_195).x
            self.get(Active7_195).values[24] = self.get(Active7_195).y
            self.get(Active7_195).values[3] = 16
            self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 3, 1, 0)
            self.get(ShotLatence_230).set_value(21)
            self.get(Accuracy_238).add_value(15+(8*self.get(Active9_222).values[7]))
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
            self.get(TestShoot_306).set_visible(False)
            self.get(AmmoCurrent_311).subtract_value(1)
            self.get(Rauch_197).force_animation('User defined 1')
            self.get(Fusssoldat_193).values[2] = 0
            self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
            self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
            self.get(Rauch_197).values[9] = 999888
            self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
            for loop_index in xrange(480):
                if self.loop_waffe1(loop_index) == False: break
            SoundAutoPlay('glock.wav')
        self.set_event_id(1192)
        if (self.groups['W3'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 3 and
        select(self.get(AmmoCurrent_311).get_value() == 0) and
        select(len(self.get(Active5_213, True)) == 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.get(ShotLatence_230).set_value(40)
            SoundAutoPlay('empty.wav')
        self.set_event_id(1193)
        if (self.groups['W3'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 3 and
        select(self.get(AmmoCurrent_311).get_value() >= 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(len(self.get(Active7_195, True)) == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
            self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
            self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
            self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
            self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
            self.get(Fusssoldat_193).values[18] = (self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 5, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value())))
            self.get(Active7_195).values[0] = cos(self.get(Fusssoldat_193).values[18])
            self.get(Active7_195).values[1] = sin(self.get(Fusssoldat_193).values[18])
            self.get(Active7_195).values[23] = self.get(Active7_195).x
            self.get(Active7_195).values[24] = self.get(Active7_195).y
            self.get(Active7_195).values[3] = 25
            self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 5, 1, 0)
            self.get(ShotLatence_230).set_value(40)
            self.get(Strafing_219).values[5] = 0
            self.get(Strafing_219).values[6] = 1
            self.get(Accuracy_238).add_value(30)
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
            self.get(TestShoot_306).set_visible(False)
            self.get(AmmoCurrent_311).subtract_value(1)
            self.get(Fusssoldat_193).values[2] = 0
            self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
            self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
            self.get(Rauch_197).values[9] = 999888
            self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('208'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'*100+3))+str(self.get(Csm_432).get_value()))
            self.function_sendall()
            self.function_csmup()
            for loop_index in xrange(400):
                if self.loop_waffe3(loop_index) == False: break
            SoundAutoPlay('m3.wav')
        self.set_event_id(1212)
        if (self.groups['W 4'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 4 and
        select(self.get(AmmoCurrent_311).get_value() == 0) and
        select(len(self.get(Active5_213, True)) == 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.get(ShotLatence_230).set_value(30)
            SoundAutoPlay('empty.wav')
        self.set_event_id(1213)
        if (self.groups['W 4'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 4 and
        select(self.get(AmmoCurrent_311).get_value() >= 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(len(self.get(Active7_195, True)) == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
            self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
            self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
            self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
            self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
            self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 6, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 6, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[23] = self.get(Active7_195).x
            self.get(Active7_195).values[24] = self.get(Active7_195).y
            self.get(Active7_195).values[3] = 27
            self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 4, 1, 0)
            self.get(ShotLatence_230).set_value(24)
            self.get(Accuracy_238).add_value(20)
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
            self.get(TestShoot_306).set_visible(False)
            self.get(AmmoCurrent_311).subtract_value(1)
            self.get(Rauch_197).force_animation('User defined 1')
            self.get(Fusssoldat_193).values[2] = 0
            self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
            self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
            self.get(Rauch_197).values[9] = 999888
            self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
            for loop_index in xrange(420):
                if self.loop_waffe4(loop_index) == False: break
            SoundAutoPlay('deagle.wav')
        self.set_event_id(1233)
        if (self.groups['W 5'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 5 and
        select(self.get(AmmoCurrent_311).get_value() == 0) and
        select(len(self.get(Active5_213, True)) == 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.get(ShotLatence_230).set_value(50)
            SoundAutoPlay('empty.wav')
        self.set_event_id(1287)
        if (self.groups['W 8'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 8 and
        select(self.get(AmmoCurrent_311).get_value() == 0) and
        select(len(self.get(Active5_213, True)) == 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.get(ShotLatence_230).set_value(25)
            SoundAutoPlay('empty.wav')
        self.set_event_id(1288)
        if (self.groups['W 8'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 8 and
        select(self.get(AmmoCurrent_311).get_value() >= 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(len(self.get(Active7_195, True)) == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
            self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
            self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
            self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
            self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
            self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 11, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 11, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[23] = self.get(Active7_195).x
            self.get(Active7_195).values[24] = self.get(Active7_195).y
            self.get(Active7_195).values[3] = 18
            self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 3, 1, 0)
            self.get(ShotLatence_230).set_value(25)
            self.get(Accuracy_238).add_value(16+(6*self.get(Active9_222).values[7]))
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
            self.get(TestShoot_306).set_visible(False)
            self.get(AmmoCurrent_311).subtract_value(1)
            self.get(Rauch_197).force_animation('User defined 1')
            self.get(Fusssoldat_193).values[2] = 0
            self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
            self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
            self.get(Rauch_197).values[9] = 999888
            self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
            for loop_index in xrange(400):
                if self.loop_waffe8(loop_index) == False: break
            SoundAutoPlay('sig.wav')
        self.set_event_id(1359)
        if (self.groups['W 12'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 12 and
        select(self.get(AmmoCurrent_311).get_value() == 0) and
        select(len(self.get(Active5_213, True)) == 0) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.get(ShotLatence_230).set_value(50)
            SoundAutoPlay('empty.wav')
        self.set_event_id(1360)
        if (self.groups['W 12'] and
        self.players[0].key_pressed(['Button1']) and
        self.players[0].lives == 12 and
        select(self.get(AmmoCurrent_311).get_value() >= 1) and
        select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
        select(self.get(ShotLatence_230).get_value() == 0) and
        select(len(self.get(Active7_195, True)) == 0) and
        select(self.get(Strafing_219).flags[9] == False)):
            self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
            self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
            self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
            self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
            self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
            self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 5, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 5, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
            self.get(Active7_195).values[23] = self.get(Active7_195).x
            self.get(Active7_195).values[24] = self.get(Active7_195).y
            self.get(Active7_195).values[3] = 51
            self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 9, 1, 0)
            self.get(ShotLatence_230).set_value(50)
            self.get(Accuracy_238).add_value(50)
            self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
            self.get(TestShoot_306).set_visible(False)
            self.get(AmmoCurrent_311).subtract_value(1)
            self.get(Fusssoldat_193).values[2] = 0
            self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
            self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
            self.get(Rauch_197).values[9] = 999888
            self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
            for loop_index in xrange(800):
                if self.loop_waffe12(loop_index) == False: break
            SoundAutoPlay('sr60.wav')
        pass
    
    def on_AnimationFinished(self, instance):
        if type(instance) == GrenadeSpot_398:
            self.set_event_id(555)
            if (self.groups['Game'] and
            select(self.get(GrenadeSpot_398).AnimationFinished(0)) and
            select(self.get(GrenadeSpot_398).values.get(1, 0) == 1)):
                self.create_object(Nade_458, self.get(GrenadeSpot_398).x + 0, self.get(GrenadeSpot_398).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(GrenadeSpot_398)', 'create_object': 'Nade_458'}
                self.get(Nade_458).set_direction(self.get(GrenadeSpot_398).values[3])
                self.get(Nade_458).SetSpeed(self.get(GrenadeSpot_398).values[18])
                self.get(Nade_458).values[1] = 1
                self.get(Nade_458).values[2] = self.get(GrenadeSpot_398).values[2]
                self.get(Nade_458).values[9] = 11110000
                self.get(GrenadeSpot_398).destroy()
                self.get(Nade_458).force_animation('User defined 1')
        if type(instance) == GrenadeSpot_398:
            self.set_event_id(557)
            if (self.groups['Game'] and
            select(self.get(GrenadeSpot_398).AnimationFinished(0)) and
            select(self.get(GrenadeSpot_398).values.get(1, 0) == 2)):
                self.create_object(Nade_458, self.get(GrenadeSpot_398).x + 0, self.get(GrenadeSpot_398).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(GrenadeSpot_398)', 'create_object': 'Nade_458'}
                self.get(Nade_458).set_direction(self.get(GrenadeSpot_398).values[3])
                self.get(Nade_458).SetSpeed(self.get(GrenadeSpot_398).values[18])
                self.get(Nade_458).values[1] = 2
                self.get(Nade_458).values[2] = self.get(GrenadeSpot_398).values[2]
                self.get(Nade_458).values[9] = 11110000
                self.get(GrenadeSpot_398).destroy()
                self.get(Nade_458).force_animation('Stopped')
        if type(instance) == GrenadeSpot_398:
            self.set_event_id(560)
            if (self.groups['Game'] and
            select(self.get(GrenadeSpot_398).AnimationFinished(0)) and
            select(self.get(GrenadeSpot_398).values.get(1, 0) == 4)):
                self.create_object(Nade2_459, self.get(GrenadeSpot_398).x + 0, self.get(GrenadeSpot_398).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(GrenadeSpot_398)', 'create_object': 'Nade2_459'}
                self.get(Nade2_459).set_direction(self.get(GrenadeSpot_398).values[3])
                self.get(Nade2_459).SetSpeed(self.get(GrenadeSpot_398).values[18])
                self.get(Nade2_459).values[2] = self.get(GrenadeSpot_398).values[2]
                self.get(Nade2_459).values[9] = 700
                self.get(GrenadeSpot_398).destroy()
                self.get(Nade2_459).values[23] = 1
        if type(instance) == GrenadeSpot_398:
            self.set_event_id(562)
            if (self.groups['Game'] and
            select(self.get(GrenadeSpot_398).AnimationFinished(0)) and
            select(self.get(GrenadeSpot_398).values.get(1, 0) == 6)):
                self.create_object(Nade2_459, self.get(GrenadeSpot_398).x + 0, self.get(GrenadeSpot_398).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(GrenadeSpot_398)', 'create_object': 'Nade2_459'}
                self.get(Nade2_459).set_direction(self.get(GrenadeSpot_398).values[3])
                self.get(Nade2_459).SetSpeed(self.get(GrenadeSpot_398).values[18])
                self.get(Nade2_459).values[2] = self.get(GrenadeSpot_398).values[2]
                self.get(Nade2_459).values[9] = 700
                self.get(GrenadeSpot_398).destroy()
                self.get(Nade2_459).values[23] = 2
        if type(instance) == GrenadeSpot_398:
            self.set_event_id(566)
            if (self.groups['Game'] and
            select(self.get(GrenadeSpot_398).AnimationFinished(0)) and
            select(self.get(GrenadeSpot_398).values.get(1, 0) == 5)):
                self.create_object(Molotov_450, self.get(GrenadeSpot_398).x + -5, self.get(GrenadeSpot_398).x + -5) # {'y': -5, 'x': -5, 'parent': 'self.get(GrenadeSpot_398)', 'create_object': 'Molotov_450'}
                self.get(Molotov_450).set_direction(self.get(GrenadeSpot_398).values[3])
                self.get(Molotov_450).SetSpeed(self.get(GrenadeSpot_398).values[18])
                self.get(Molotov_450).values[1] = 1
                self.get(Molotov_450).values[2] = self.get(GrenadeSpot_398).values[2]
                self.get(Molotov_450).values[9] = 11110000
                self.get(GrenadeSpot_398).destroy()
        if type(instance) == Explode_453:
            self.set_event_id(606)
            if (self.groups['Game'] and
            select(self.get(Explode_453).AnimationFinished(0))):
                self.get(Explode_453).destroy()
        if type(instance) == SmokeExp_460:
            self.set_event_id(614)
            if (self.groups['Game'] and
            select(self.get(SmokeExp_460).AnimationFinished(0))):
                self.get(SmokeExp_460).destroy()
        if type(instance) == ActiveObject1_218:
            self.set_event_id(688)
            if (self.groups['Game'] and
            select(self.get(ActiveObject1_218).AnimationFinished(0))):
                self.get(ActiveObject1_218).destroy()
        if type(instance) == Destroy_375:
            self.set_event_id(784)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).AnimationFinished(0))):
                self.get(Destroy_375).destroy()
        if type(instance) == HitBack_198:
            self.set_event_id(787)
            if (self.groups['Game'] and
            select(self.get(HitBack_198).AnimationFinished(0))):
                self.get(HitBack_198).destroy()
        if type(instance) == Obj1Die_255:
            self.set_event_id(1463)
            if (self.groups['Graphic reduced 2'] and
            select(self.get(Obj1Die_255).AnimationFinished(0))):
                self.get(Obj1Die_255).destroy()
        if type(instance) == Obj2Die_199:
            self.set_event_id(1464)
            if (self.groups['Graphic reduced 2'] and
            select(self.get(Obj2Die_199).AnimationFinished(0))):
                self.get(Obj2Die_199).destroy()
        if type(instance) == Obj3Die_338:
            self.set_event_id(1465)
            if (self.groups['Graphic reduced 2'] and
            select(self.get(Obj3Die_338).AnimationFinished(0))):
                self.get(Obj3Die_338).destroy()
        if type(instance) == Obj6Die_341:
            self.set_event_id(1466)
            if (self.groups['Graphic reduced 2'] and
            select(self.get(Obj6Die_341).AnimationFinished(0))):
                self.get(Obj6Die_341).destroy()
        if type(instance) == Obj4Die_339:
            self.set_event_id(1467)
            if (self.groups['Graphic reduced 2'] and
            select(self.get(Obj4Die_339).AnimationFinished(0))):
                self.get(Obj4Die_339).destroy()
        if type(instance) == Obj5Die_340:
            self.set_event_id(1468)
            if (self.groups['Graphic reduced 2'] and
            select(self.get(Obj5Die_340).AnimationFinished(0))):
                self.get(Obj5Die_340).destroy()
        if type(instance) == Obj1Die_255:
            self.set_event_id(1473)
            if (self.groups['Graphic reduced 3'] and
            select(self.get(Obj1Die_255).AnimationFinished(0))):
                self.get(Obj1Die_255).destroy()
        if type(instance) == Obj2Die_199:
            self.set_event_id(1474)
            if (self.groups['Graphic reduced 3'] and
            select(self.get(Obj2Die_199).AnimationFinished(0))):
                self.get(Obj2Die_199).destroy()
        if type(instance) == Obj3Die_338:
            self.set_event_id(1475)
            if (self.groups['Graphic reduced 3'] and
            select(self.get(Obj3Die_338).AnimationFinished(0))):
                self.get(Obj3Die_338).destroy()
        if type(instance) == Obj6Die_341:
            self.set_event_id(1476)
            if (self.groups['Graphic reduced 3'] and
            select(self.get(Obj6Die_341).AnimationFinished(0))):
                self.get(Obj6Die_341).destroy()
        if type(instance) == Obj4Die_339:
            self.set_event_id(1477)
            if (self.groups['Graphic reduced 3'] and
            select(self.get(Obj4Die_339).AnimationFinished(0))):
                self.get(Obj4Die_339).destroy()
        if type(instance) == Obj5Die_340:
            self.set_event_id(1478)
            if (self.groups['Graphic reduced 3'] and
            select(self.get(Obj5Die_340).AnimationFinished(0))):
                self.get(Obj5Die_340).destroy()
        pass
    
    def on_LeavingPlayfield(self, instance):
        if type(instance) == Strafing_219:
            self.set_event_id(1074)
            if (self.groups['Custom Movement'] and
            select(self.get(Strafing_219).LeavingPlayfield(15))):
                self.get(Fusssoldat_193).values[21] = 8
                self.get(Strafing_219).movement.stop()
                self.get(Strafing_219).set_position(x = self.get(TrackX_268).get_value())
                self.get(Strafing_219).set_position(y = self.get(TrackY_269).get_value())
                self.get(Strafing_219).values[18] = 'self.get(Strafing_219).GetDirection'
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
        if type(instance) == Strafing2_220:
            self.set_event_id(1142)
            if (self.groups['Dead Reckoning'] and
            select(self.get(Strafing2_220).LeavingPlayfield(15)) and
            select(self.get(Strafing2_220).values.get(23, 0) == 0) and
            select(self.get(Strafing2_220).values.get(24, 0) == 0)):
                self.get(Strafing2_220).values[4] = 0
                self.get(Strafing2_220).movement.stop()
        if type(instance) == Nade2_459:
            self.set_event_id(1147)
            if (self.groups['Dead Reckoning'] and
            select(self.get(Nade2_459).LeavingPlayfield(15))):
                self.get(Nade2_459).Bounce()
        pass
    
    def on_PathFinished(self, instance):
        if type(instance) == Frantic_248:
            self.set_event_id(684)
            if (self.groups['Game'] and
            select(self.get(Frantic_248).PathFinished())):
                self.get(Frantic_248).destroy()
        if type(instance) == Daunting_249:
            self.set_event_id(685)
            if (self.groups['Game'] and
            select(self.get(Daunting_249).PathFinished())):
                self.get(Daunting_249).destroy()
        if type(instance) == Godlike_250:
            self.set_event_id(686)
            if (self.groups['Game'] and
            select(self.get(Godlike_250).PathFinished())):
                self.get(Godlike_250).destroy()
        if type(instance) == Cp2_435:
            self.set_event_id(1497)
            if (self.groups['Speed Hack'] and
            select(self.get(Cp2_435).PathFinished()) and
            select(self.get(Cp2c_436).get_value() > 100)):
                self.get(ServerError_60).set_value('Speed hack detected!')
                self.set_frame(4)
        if type(instance) == Cp2_435:
            self.set_event_id(1498)
            if (self.groups['Speed Hack'] and
            select(self.get(Cp2_435).PathFinished())):
                self.get(Cp2_435).destroy()
                self.groups['Speed Hack'] = False
        pass
    
    def on_OnCollision(self, instance):
        if type(instance) == Flash_380:
            self.set_event_id(563)
            if (self.groups['Game'] and
            select(self.get(Flash_380).OnCollision(Strafing_219)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
                self.get(FlashTime_381).set_value(self.get(Flash_380).values[1])
                self.get(Flash_380).destroy()
                self.get(Accuracy_238).set_value(50)
                self.groups['Flashed'] = True
        if type(instance) == Flash_380:
            self.set_event_id(564)
            if (self.groups['Game'] and
            select(self.get(Flash_380).OnCollision(Strafing_219)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 0)):
                self.get(Flash_380).destroy()
        if type(instance) == AmmoPack_208:
            self.set_event_id(653)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            self.players[0].lives == 1):
                self.get(Ammo1_321).set_value(self.get(AmmoCurrent_311).get_value())
        if type(instance) == AmmoPack_208:
            self.set_event_id(654)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            self.players[0].lives == 8):
                self.get(Ammo1_321).set_value(self.get(AmmoCurrent_311).get_value())
        if type(instance) == AmmoPack_208:
            self.set_event_id(655)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 0) and
            'self.get(WeaponList_320).ListGetLineCount' > 0):
                self.players[0].lives = to_number(self.get(WeaponList_320).get_line(randrange('self.get(WeaponList_320).ListGetLineCount')+1))
                self.groups['Weapon Change'] = True
                self.get(AmmoPack_208).destroy()
                SoundAutoPlay('collect.wav')
        if type(instance) == AmmoPack_208:
            self.set_event_id(656)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 28) and
            'self.get(WeaponList_320).ListGetLineCount' > 0):
                self.players[0].lives = to_number(self.get(WeaponList_320).get_line(randrange('self.get(WeaponList_320).ListGetLineCount')+1))
                self.groups['Weapon Change'] = True
                self.get(AmmoPack_208).destroy()
                SoundAutoPlay('collect.wav')
        if type(instance) == AmmoPack_208:
            self.set_event_id(657)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 24) and
            'self.get(WeaponList_320).ListGetLineCount' > 0):
                self.players[0].lives = to_number(self.get(WeaponList_320).get_line(randrange('self.get(WeaponList_320).ListGetLineCount')+1))
                self.groups['Weapon Change'] = True
                self.get(AmmoPack_208).destroy()
                SoundAutoPlay('collect.wav')
        if type(instance) == AmmoPack_208:
            self.set_event_id(658)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing2_220))):
                self.get(AmmoPack_208).destroy()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('collect.wav', self.get(AmmoPack_208).x, self.get(AmmoPack_208).y)
        if type(instance) == AmmoPack_208:
            self.set_event_id(659)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 4) and
            select(self.get(Fusssoldat_193).values.get(5, 0) >= 60) and
            self.get_global_value(1) == 0):
                self.get(Fusssoldat_193).values[5] = 100
                self.get(AmmoPack_208).destroy()
                self.get(Msg_427).set_value('109'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('collect.wav')
        if type(instance) == AmmoPack_208:
            self.set_event_id(660)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 4) and
            select(self.get(Fusssoldat_193).values.get(5, 0) < 60) and
            self.get_global_value(1) == 0):
                self.get(Fusssoldat_193).AddToAlterable(5, 40)
                self.get(AmmoPack_208).destroy()
                self.get(Msg_427).set_value('109'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('collect.wav')
        if type(instance) == AmmoPack_208:
            self.set_event_id(661)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 4) and
            select(self.get(Fusssoldat_193).values.get(5, 0) >= 60) and
            self.get_global_value(1) == 1):
                self.get(Fusssoldat_193).values[5] = 100
                self.get(AmmoPack_208).destroy()
                SoundAutoPlay('collect.wav')
        if type(instance) == AmmoPack_208:
            self.set_event_id(662)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 4) and
            select(self.get(Fusssoldat_193).values.get(5, 0) < 60) and
            self.get_global_value(1) == 1):
                self.get(Fusssoldat_193).AddToAlterable(5, 40)
                self.get(AmmoPack_208).destroy()
                SoundAutoPlay('collect.wav')
        if type(instance) == AmmoPack_208:
            self.set_event_id(663)
            if (self.groups['Game'] and
            select(self.get(AmmoPack_208).OnCollision(Strafing_219)) and
            select(self.get(AmmoPack_208).direction_value == 8)):
                self.get(Fusssoldat_193).values[12] = randrange(2)+1
                self.get(AmmoPack_208).destroy()
                self.groups['Grenades'] = True
                SoundAutoPlay('collect.wav')
        if type(instance) == Destroy_375:
            self.set_event_id(771)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(qualifier_6))):
                self.create_object(WallDestroyed_376, self.get(qualifier_6).x + 0, self.get(qualifier_6).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(qualifier_6)', 'create_object': 'WallDestroyed_376'}
                self.get(WallDestroyed_376).BringToBack()
                self.get(WallDestroyed_376).values[9] = (1000000+self.get(WallDestroyed_376).y*1000+self.get(WallDestroyed_376).x)*-1
        if type(instance) == Destroy_375:
            self.set_event_id(772)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall11_300))):
                self.get(Wall11_300).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(773)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall12_301))):
                self.get(Wall12_301).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(774)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall21_302))):
                self.get(Wall21_302).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(775)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall22_303))):
                self.get(Wall22_303).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(776)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall13_407))):
                self.get(Wall13_407).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(777)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall14_408))):
                self.get(Wall14_408).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(778)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall23_409))):
                self.get(Wall23_409).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(779)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Wall24_410))):
                self.get(Wall24_410).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(780)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Box_287))):
                self.create_object(BoxDestroyed_377, self.get(Box_287).x + 0, self.get(Box_287).x + 8) # {'y': 8, 'x': 0, 'parent': 'self.get(Box_287)', 'create_object': 'BoxDestroyed_377'}
                self.get(BoxDestroyed_377).BringToBack()
                self.get(BoxDestroyed_377).values[9] = (1000000+self.get(BoxDestroyed_377).y*1000+self.get(BoxDestroyed_377).x)*-1
                self.get(Box_287).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(781)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(Pipeline_403))):
                self.create_object(PipelineDestroyed_411, self.get(Pipeline_403).x + 0, self.get(Pipeline_403).x + 10) # {'y': 10, 'x': 0, 'parent': 'self.get(Pipeline_403)', 'create_object': 'PipelineDestroyed_411'}
                self.get(PipelineDestroyed_411).BringToBack()
                self.get(PipelineDestroyed_411).values[9] = (1000000+self.get(PipelineDestroyed_411).y*1000+self.get(PipelineDestroyed_411).x)*-1
                self.get(Pipeline_403).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(782)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(PoliceCar_275))):
                self.get(PoliceCar_275).force_animation('User defined 1')
        if type(instance) == Destroy_375:
            self.set_event_id(783)
            if (self.groups['Game'] and
            select(self.get(Destroy_375).OnCollision(PoliceCar2_276))):
                self.get(PoliceCar2_276).force_animation('User defined 1')
        if type(instance) == Fusssoldat2_194:
            self.set_event_id(816)
            if (self.groups['Client'] and
            select(self.get(Fusssoldat2_194).OnCollision(Exp_247)) and
            select(self.get(Exp_247).values.get(23, 0) != self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(Exp_247).values.get(2, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(Exp_247).AnimationFrame(9))):
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((50+randrange(6)+self.get(Fusssoldat2_194).values[12]*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Exp_247).values[23] = self.get(Fusssoldat2_194).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        if type(instance) == Fusssoldat_193:
            self.set_event_id(817)
            if (self.groups['Client'] and
            select(self.get(Fusssoldat_193).OnCollision(Exp_247)) and
            select(self.get(Exp_247).values.get(23, 0) != self.get(Fusssoldat_193).values[0]) and
            select(self.get(Exp_247).values.get(2, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(Exp_247).AnimationFrame(9))):
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat_193).values[11] = 50+randrange(6)
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[11]
                self.get(Fusssoldat_193).values[6] = 10
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[11]+self.get(VisibleId_424).get_value()*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Exp_247).values[23] = self.get(Fusssoldat_193).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
        if type(instance) == Fusssoldat2_194:
            self.set_event_id(818)
            if (self.groups['Client'] and
            select(self.get(Fusssoldat2_194).OnCollision(FlameDmg_456)) and
            select(self.get(FlameDmg_456).values.get(23, 0) != self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(FlameDmg_456).values.get(1, 0) == self.get(Fusssoldat_193).values[0])):
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((18+randrange(5)+self.get(Fusssoldat2_194).values[12]*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(FlameDmg_456).values[23] = self.get(Fusssoldat2_194).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        if type(instance) == Fusssoldat_193:
            self.set_event_id(819)
            if (self.groups['Client'] and
            select(self.get(Fusssoldat_193).OnCollision(FlameDmg_456)) and
            select(self.get(FlameDmg_456).values.get(23, 0) != self.get(Fusssoldat_193).values[0]) and
            select(self.get(FlameDmg_456).values.get(1, 0) == self.get(Fusssoldat_193).values[0])):
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat_193).values[11] = 18+randrange(5)
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[11]
                self.get(Fusssoldat_193).values[6] = 10
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[11]+self.get(VisibleId_424).get_value()*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(FlameDmg_456).values[23] = self.get(Fusssoldat_193).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
        if type(instance) == Fusssoldat2_194:
            self.set_event_id(820)
            if (self.groups['Client'] and
            select(self.get(Fusssoldat2_194).OnCollision(BigflameDmg_457)) and
            select(self.get(BigflameDmg_457).values.get(23, 0) != self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(BigflameDmg_457).values.get(2, 0) == self.get(Fusssoldat_193).values[0])):
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((100+self.get(Fusssoldat2_194).values[12]*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(BigflameDmg_457).values[23] = self.get(Fusssoldat2_194).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        if type(instance) == Fusssoldat_193:
            self.set_event_id(821)
            if (self.groups['Client'] and
            select(self.get(Fusssoldat_193).OnCollision(BigflameDmg_457)) and
            select(self.get(BigflameDmg_457).values.get(23, 0) != self.get(Fusssoldat_193).values[0]) and
            select(self.get(BigflameDmg_457).values.get(2, 0) == self.get(Fusssoldat_193).values[0])):
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat_193).values[11] = 100
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[11]
                self.get(Fusssoldat_193).values[6] = 10
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[11]+self.get(VisibleId_424).get_value()*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(BigflameDmg_457).values[23] = self.get(Fusssoldat_193).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
        if type(instance) == Fusssoldat_193:
            self.set_event_id(832)
            if (self.groups['Overlayer'] and
            select(self.get(Fusssoldat_193).OnCollision(qualifier_1))):
                self.groups['Layer'] = True
        if type(instance) == Fusssoldat2_194:
            self.set_event_id(962)
            if (self.groups['Server'] and
            select(self.get(Fusssoldat2_194).OnCollision(Exp_247)) and
            select(self.get(Exp_247).values.get(23, 0) != self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(Exp_247).values.get(2, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(Exp_247).AnimationFrame(9)) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat2_194).values[11] = 50+randrange(6)
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat2_194).values[11] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat2_194).values[11], 0)
                self.get(Fusssoldat2_194).values[24] -= self.get(Fusssoldat2_194).values[11]
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[11]+self.get(Fusssoldat2_194).values[12]*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat2_194).values[5] = 2
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(Exp_247).values[23] = self.get(Fusssoldat2_194).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        if type(instance) == Fusssoldat_193:
            self.set_event_id(963)
            if (self.groups['Server'] and
            select(self.get(Fusssoldat_193).OnCollision(Exp_247)) and
            select(self.get(Exp_247).values.get(23, 0) != self.get(Fusssoldat_193).values[0]) and
            select(self.get(Exp_247).values.get(2, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(Exp_247).AnimationFrame(9)) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat_193).values[11] = 50+randrange(6)
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat_193).values[25] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat_193).values[11] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat_193).values[11], 0)
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[11]
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[11]+self.get(VisibleId_424).get_value()*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat_193).values[16] = 2
                self.get(Fusssoldat_193).values[6] = 10
                self.get(Exp_247).values[23] = self.get(Fusssoldat_193).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
        if type(instance) == Fusssoldat2_194:
            self.set_event_id(964)
            if (self.groups['Server'] and
            select(self.get(Fusssoldat2_194).OnCollision(FlameDmg_456)) and
            select(self.get(FlameDmg_456).values.get(23, 0) != self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(FlameDmg_456).values.get(1, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat2_194).values[11] = 18+randrange(5)
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat2_194).values[11] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat2_194).values[11], 0)
                self.get(Fusssoldat2_194).values[24] -= self.get(Fusssoldat2_194).values[11]
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[11]+self.get(Fusssoldat2_194).values[12]*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat2_194).values[5] = 2
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(FlameDmg_456).values[23] = self.get(Fusssoldat2_194).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        if type(instance) == Fusssoldat_193:
            self.set_event_id(965)
            if (self.groups['Server'] and
            select(self.get(Fusssoldat_193).OnCollision(FlameDmg_456)) and
            select(self.get(FlameDmg_456).values.get(23, 0) != self.get(Fusssoldat_193).values[0]) and
            select(self.get(FlameDmg_456).values.get(1, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat_193).values[11] = 18+randrange(5)
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat_193).values[25] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat_193).values[11] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat_193).values[11], 0)
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[11]
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[11]+self.get(VisibleId_424).get_value()*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat_193).values[16] = 2
                self.get(Fusssoldat_193).values[6] = 10
                self.get(FlameDmg_456).values[23] = self.get(Fusssoldat_193).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
        if type(instance) == Fusssoldat2_194:
            self.set_event_id(966)
            if (self.groups['Server'] and
            select(self.get(Fusssoldat2_194).OnCollision(BigflameDmg_457)) and
            select(self.get(BigflameDmg_457).values.get(23, 0) != self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(BigflameDmg_457).values.get(2, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat2_194).values[11] = 100
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat2_194).values[11] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat2_194).values[11], 0)
                self.get(Fusssoldat2_194).values[24] -= self.get(Fusssoldat2_194).values[11]
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[11]+self.get(Fusssoldat2_194).values[12]*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat2_194).values[5] = 2
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(BigflameDmg_457).values[23] = self.get(Fusssoldat2_194).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        if type(instance) == Fusssoldat_193:
            self.set_event_id(967)
            if (self.groups['Server'] and
            select(self.get(Fusssoldat_193).OnCollision(BigflameDmg_457)) and
            select(self.get(BigflameDmg_457).values.get(23, 0) != self.get(Fusssoldat_193).values[0]) and
            select(self.get(BigflameDmg_457).values.get(2, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat_193).values[11] = 100
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat_193).values[25] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat_193).values[11] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat_193).values[11], 0)
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[11]
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[11]+self.get(VisibleId_424).get_value()*1000+200000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat_193).values[16] = 2
                self.get(Fusssoldat_193).values[6] = 10
                self.get(BigflameDmg_457).values[23] = self.get(Fusssoldat_193).values[0]
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
        if type(instance) == Strafing_219:
            self.set_event_id(1070)
            if (self.groups['Custom Movement'] and
            select(self.get(Strafing_219).OnCollision(qualifier_2)) and
            select(self.get(Strafing_219).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Fusssoldat_193).values[21] = 8
                self.get(Strafing_219).movement.stop()
                self.get(Strafing_219).set_position(x = self.get(TrackX_268).get_value())
                self.get(Strafing_219).set_position(y = self.get(TrackY_269).get_value())
                self.get(Strafing_219).values[18] = 'self.get(Strafing_219).GetDirection'
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
        if type(instance) == Strafing_219:
            self.set_event_id(1072)
            if (self.groups['Custom Movement'] and
            select(self.get(Strafing_219).OnCollision(qualifier_3))):
                self.get(Fusssoldat_193).values[21] = 8
                self.get(Strafing_219).movement.stop()
                self.get(Strafing_219).set_position(x = self.get(TrackX_268).get_value())
                self.get(Strafing_219).set_position(y = self.get(TrackY_269).get_value())
                self.get(Strafing_219).values[18] = 'self.get(Strafing_219).GetDirection'
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
        if type(instance) == Strafing2_220:
            self.set_event_id(1140)
            if (self.groups['Dead Reckoning'] and
            select(self.get(Strafing2_220).OnCollision(qualifier_2)) and
            select(self.get(Strafing2_220).values.get(9, 0) >= self.get(qualifier_2).values[9]) and
            select(self.get(Strafing2_220).values.get(23, 0) == 0) and
            select(self.get(Strafing2_220).values.get(24, 0) == 0)):
                self.get(Strafing2_220).values[4] = 0
                self.get(Strafing2_220).movement.stop()
        if type(instance) == Strafing2_220:
            self.set_event_id(1141)
            if (self.groups['Dead Reckoning'] and
            select(self.get(Strafing2_220).OnCollision(qualifier_3)) and
            select(self.get(Strafing2_220).values.get(23, 0) == 0) and
            select(self.get(Strafing2_220).values.get(24, 0) == 0)):
                self.get(Strafing2_220).values[4] = 0
                self.get(Strafing2_220).movement.stop()
        if type(instance) == Nade2_459:
            self.set_event_id(1148)
            if (self.groups['Dead Reckoning'] and
            select(self.get(Nade2_459).OnCollision(qualifier_2)) and
            select(self.get(Nade2_459).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Nade2_459).values[19] = 0
                self.get(Nade2_459).Bounce()
        if type(instance) == Nade2_459:
            self.set_event_id(1149)
            if (self.groups['Dead Reckoning'] and
            select(self.get(Nade2_459).OnCollision(qualifier_3))):
                self.get(Nade2_459).values[19] = 0
                self.get(Nade2_459).Bounce()
        if type(instance) == FlameDmg_456:
            self.set_event_id(1152)
            if (self.groups['Dead Reckoning'] and
            select(self.get(FlameDmg_456).OnCollision(qualifier_3)) and
            select(self.get(Active17_451).values.get(4, 0) == 'self.get(FlameDmg_456).FixedValue')):
                self.create_object(Explode_453, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'Explode_453'}
                self.get(Explode_453).values[9] = 11100000
                self.get(Active17_451).destroy()
                self.get(FlameDmg_456).destroy()
        if type(instance) == AmmoTest_319:
            self.set_event_id(1383)
            if (self.groups['Crates'] and
            select(self.get(AmmoTest_319).OnCollision(qualifier_1))):
                self.get(AmmoTest_319).destroy()
        if type(instance) == AmmoTest_319:
            self.set_event_id(1384)
            if (self.groups['Crates'] and
            select(self.get(AmmoTest_319).OnCollision(AmmoPack_208))):
                self.get(AmmoTest_319).destroy()
        pass

    def on_EndOfFrame(self, instance):
        self.set_event_id(39)
        if (EndOfFrame() and
        self.get_global_value(12) == 1):
            self.values[12] = 2
            self.stop_mod(self.get(ModMusic_391).get_value())
        self.set_event_id(540)
        if (self.groups['Game'] and
        EndOfFrame()):
            self.get(Moo_181).disconnect()
            BlowfishRemoveKey(self.get(Sting_186).text)
            self.get(Sting_186).set_value('Text')
        pass

    def add_hud_line(self, value):
        self.get(Message1_205).set_value(self.get(Message2_206).text)
        self.get(Message2_206).set_value(self.get(Message3_207).text)
        self.get(Message3_207).set_value(self.get(Message4_243).text)
        self.get(Message4_243).set_value(value)
    
    def update(self, dt):
        self.set_event_id(14)
        if (Qt.Key_F12 in self.scene.key_presses and
        self.get_global_value(1) == 0):
            self.set_frame(2)
        self.set_event_id(15)
        if (Qt.Key_F12 in self.scene.key_presses and
        self.get_global_value(1) == 1 and
        select(self.get(ExitCounter_221).get_value() == 0)):
            self.get(ExitCounter_221).set_value(4)
            self.get(ChangeMap_217).set_visible(True)
            self.get(ChangeMap_217).set_value('Closing server...')
            self.add_hud_line('Closing server')
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Fusssoldat_193).values[22] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('108')
            self.function_sendall()
            self.get(Edit2_336).set_value('GET http://www.seekanddread.de/Game/svr_del.php'+' HTTP/1.0'+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
            ResetGlobalTimer(0)
            self.get(MooSock_335).connect('www.seekanddread.de', 80)
            self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+',,'+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
        self.set_event_id(16)
        if (Qt.Key_Escape in self.scene.key_presses and
        self.get_global_value(1) == 0):
            self.set_frame(2)
        self.set_event_id(17)
        if (Qt.Key_Escape in self.scene.key_presses and
        self.get_global_value(1) == 1 and
        select(self.get(ExitCounter_221).get_value() == 0)):
            self.get(ExitCounter_221).set_value(4)
            self.get(ChangeMap_217).set_visible(True)
            self.get(ChangeMap_217).set_value('Closing server...')
            self.add_hud_line('Closing server')
            self.get(DurchlaufChat_245).set_value(0)
            self.get(Fusssoldat_193).values[22] = 0
            self.get(NotID_430).set_value(0)
            self.get(Msg_427).set_value('108')
            self.function_sendall()
            self.get(Edit2_336).set_value('GET http://www.seekanddread.de/Game/svr_del.php'+' HTTP/1.0'+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
            ResetGlobalTimer(0)
            self.get(MooSock_335).connect('www.seekanddread.de', 80)
            self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+',,'+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
        self.set_event_id(18)
        if (self.every(1.0) and
        select(self.get(ExitCounter_221).get_value() > 1)):
            self.get(ExitCounter_221).subtract_value(1)
        self.set_event_id(19)
        if select(self.get(ExitCounter_221).get_value() == 1):
            self.set_frame(2)
        self.set_event_id(34)
        if Qt.Key_F8 in self.scene.key_presses:
            self.capture_filename = 'screenshot'+str(self.get(ScreenshotNr_23).get_value())+'.bmp'
        self.set_event_id(35)
        if Qt.Key_F8 in self.scene.key_presses:
            CaptureFrame()
            self.capture_filename = 'screenshot'+str(self.get(ScreenshotNr_23).get_value())+'.bmp'
            CaptureStartAutomatic()
            self.get(ScreenshotNr_23).add_value(1)
            self.get(Strafing_219).flags[1] = True
        self.set_event_id(38)
        if select(self.get(Strafing_219).flags[1] == True):
            self.get(Strafing_219).flags[1] = False
            os.remove('Screenshot.pak')
            open('Screenshot.pak', "wb").close()
            fp = open('Screenshot.pak', "ab")
            fp.write(str(self.get(ScreenshotNr_23).get_value()))
            fp.close()
        if self.groups['Server main']:
            self.set_event_id(48)
            if self.check_once():
                self.add_hud_line('Server started')
                self.get(ChangeMap_217).set_value(self.get(MessageOfDay_58).text)
                self.get(ChangeMap_217).set_visible(True)
                self.groups['Load Map'] = True
                self.groups['Crates'] = True
            self.set_event_id(49)
            if self.check_once():
                self.get(Fusssoldat_193).values[0] = 1
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
            self.set_event_id(164)
            if self.every(15.0):
                for loop_index in xrange('self.get(Moo_181).SockCountSockets'-1):
                    if self.loop_timeout(loop_index) == False: break
                for loop_index in xrange('self.get(Moo2_447).SockCountSockets'-1):
                    if self.loop_timeout2(loop_index) == False: break
            self.set_event_id(167)
            if self.every(20.0):
                self.get(Timeout1_448).reset()
                for loop_index in xrange('self.get(Moo_181).SockCountSockets'-1):
                    if self.loop_check_timeout(loop_index) == False: break
                for loop_index in xrange('self.get(Timeout1_448).ListGetLineCount'):
                    if self.loop_kick_timeout(loop_index) == False: break
                self.get(Timeout1_448).reset()
                for loop_index in xrange('self.get(Moo2_447).SockCountSockets'-1):
                    if self.loop_check_timeout2(loop_index) == False: break
                for loop_index in xrange('self.get(Timeout1_448).ListGetLineCount'):
                    if self.loop_kick_timeout2(loop_index) == False: break
        if self.groups['Music']:
            self.set_event_id(375)
            if self.every(210.0):
                self.stop_mod(self.get(ModMusic_391).get_value(), 3000) # with fade
                self.get(ModMusic_391).set_value(self.get(ModMusic_391).get_value()-(randrange(3)+1))
                self.get(ModMusic_391).set_value(immediate_compare(self.get(ModMusic_391).get_value(), '<', 1, self.get(ModMusic_391).get_value()+4, self.get(ModMusic_391).get_value()))
                ModulePlay(self.get(ModMusic_391).get_value())
            self.set_event_id(376)
            if self.check_once():
                self.get(ModMusic_391).set_value(randrange(4)+1)
                self.cross_fade_mod(self.get(ModMusic_391).get_value(), self.get(ModMusic_391).get_value(), 3000)
        if self.groups['Load Map']:
            self.set_event_id(379)
            if True:
                self.get(XtraXtraCRC_182).calculate(self.get(ChosedMap_125).text)
                self.get(Mapid_397).set_value(str(self.get(XtraXtraCRC_182).get_crc()))
                self.groups['Speed Hack'] = False
                for item in self.get(Cp2_435, True):
                    item.destroy()
                self.get(Respawn_201).set_value(20)
                self.get(Respawn_201).set_visible(False)
                self.get(String2_200).set_visible(False)
                self.get(Reclist_426).reset()
            self.set_event_id(380)
            if True:
                decrypt_file(self.get(ChosedMap_125).text, 8)
                self.get(LoadMap_259).reset()
                self.get(BackgroundX_261).set_value(0)
                self.get(BackgroundY_262).set_value(0)
                self.get(FlashTime_381).set_value(0)
                self.create_object(Stone_267, 342, -103) # {'y': -103, 'x': 342, 'create_object': 'Stone_267'}
                self.get(OverlayRedux2_443).clear(0, 0, 0)
            self.set_event_id(381)
            if True:
                self.get(LoadMap_259).load(self.get(ChosedMap_125).text)
            self.set_event_id(382)
            if (True and
            self.get_global_value(1) == 1):
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('223'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(383)
            if True:
                self.get(Modestatus_413).set_value(to_number(self.get(LoadMap_259).get_line(3)))
                for loop_index in xrange(self.get(LoadMap_259).get_count()):
                    if self.loop_load(loop_index) == False: 
                        break
        if self.groups['Add server']:
            self.set_event_id(491)
            if self.get_timer(0) >= 270000:
                self.get(Edit2_336).set_value(self.get(ServerName_100).text+','+self.get(ChosedMapWithoutPath_126).text+','+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(HostIP_150).text+','+self.get(Port_47).text+','+self.get(Version_26).text+','+immediate_compare(self.get(SvrPw_155).text, '=', ' ', '0', '1'))
                self.get(BinaryObject_38).insert(self.get(Edit2_336).get_value(), 0)
                self.get(BinaryObject_38).BinaryEncodeBase64()
                self.get(BinaryObject_38).replace('+', '-')
                self.get(BinaryObject_38).replace('/', '_')
                self.get(BinaryObject_38).replace('=', '.')
                self.get(BinaryObject_38).replace('\n', '')
                self.get(BinaryObject_38).replace('\r', '')
                self.get(Edit2_336).set_value(self.get(BinaryObject_38).get_string(0, self.get(BinaryObject_38).get_size()))
                self.get(BinaryObject_38).clear()
                self.get(Edit2_336).set_value('GET http://www.seekanddread.de/Game/svr_add.php?sndserver='+self.get(Edit2_336).get_value()+' HTTP/1.0')
                self.get(Edit2_336).set_value(self.get(Edit2_336).get_value()+'\r\n'+'Host: www.seekanddread.de'+'\r\n'+'From: webmaster@seekanddread.de'+'\r\n'+'User-Agent: HTTPTool/1.0'+'\r\n'+'\r\n')
                self.get(MooSock_335).connect('www.seekanddread.de', 80)
                ResetGlobalTimer(0)
                self.get_timer(0).stop()
        if self.groups['Background']:
            self.set_event_id(495)
            if (self.check_once() and
            select(len(self.get(SpawnArea_192, True)) == 0) and
            select(len(self.get(PoliceSpawn_345, True)) >= 1) and
            select(len(self.get(TerrorSpawn_346, True)) >= 1) and
            select(self.get(Modestatus_413).get_value() == 1)):
                self.get(Mode_344).set_value(1)
                self.get(Respawn_201).set_value(9)
                self.get(Cash_364).set_visible(True)
                self.get(_365).set_visible(True)
                self.get(Score_367).set_visible(True)
                self.get(Money_366).set_visible(True)
                self.get(ScorePolice_368).set_visible(True)
                self.get(ScoreTerror_369).set_visible(True)
                self.groups['Crates'] = False
                self.get(AmmoPack_208).destroy()
                self.get(DM_412).set_value(0)
            self.set_event_id(496)
            if (self.check_once() and
            select(self.get(Modestatus_413).get_value() == 2)):
                self.get(Mode_344).set_value(1)
                self.get(Respawn_201).set_value(9)
                self.get(Cash_364).set_visible(True)
                self.get(_365).set_visible(True)
                self.get(Score_367).set_visible(True)
                self.get(Money_366).set_visible(True)
                self.get(ScorePolice_368).set_visible(True)
                self.get(ScoreTerror_369).set_visible(True)
                self.groups['Crates'] = False
                for item in self.get(AmmoPack_208, True):
                    item.destroy()
                self.get(DM_412).set_value(0)
            self.set_event_id(497)
            if (self.check_once() and
            select(self.get(Modestatus_413).get_value() == 3)):
                self.get(Mode_344).set_value(1)
                self.get(Respawn_201).set_value(9)
                self.get(Score_367).set_visible(True)
                self.get(ScorePolice_368).set_visible(True)
                self.get(ScoreTerror_369).set_visible(True)
            self.set_event_id(498)
            if (self.check_once() and
            self.get_global_value(1) == 1 and
            select(self.get(SpawnArea_192).NumberOfObjects(0)) and
            select(self.get(PoliceSpawn_345).NumberOfObjects(1)) and
            select(self.get(TerrorSpawn_346).NumberOfObjects(1)) and
            select(self.get(Modestatus_413).get_value() == 1)):
                self.get(Respawn_201).set_value(9)
                self.get(Police_342).set_visible(True)
                self.get(Terror_343).set_visible(True)
                self.groups['Join Team'] = True
                self.get(DM_412).set_value(0)
            self.set_event_id(499)
            if (self.check_once() and
            self.get_global_value(1) == 1 and
            select(self.get(Modestatus_413).get_value() == 2)):
                self.get(Respawn_201).set_value(9)
                self.get(Police_342).set_visible(True)
                self.get(Terror_343).set_visible(True)
                self.groups['Join Team'] = True
                self.get(DM_412).set_value(0)
            self.set_event_id(500)
            if (self.check_once() and
            self.get_global_value(1) == 1 and
            select(self.get(Modestatus_413).get_value() == 3)):
                self.get(Respawn_201).set_value(9)
                self.get(Police_342).set_visible(True)
                self.get(Terror_343).set_visible(True)
                self.groups['Join Team'] = True
            self.set_event_id(501)
            if (self.check_once() and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 0) and
            select(self.get(Mode_344).get_value() == 0)):
                self.get(String2_200).set_visible(True)
                self.get(Respawn_201).set_visible(True)
            self.set_event_id(502)
            if self.players[1].lives == 1:
                count = 0
                for klass in DISPLAY_CLASSES:
                    for item in self.get(klass, True):
                        item.values[11] = count
                        count += 1
                self.get(Strafing_219).values[22] = count
            self.set_event_id(503)
            if self.players[1].lives == 1:
                for loop_index in xrange(len(self.get(qualifier_99, True))):
                    if self.loop_drawback(loop_index) == False: break
            self.set_event_id(518)
            for klass in DISPLAY_CLASSES:
                for item in self.get(klass, True):
                    if item.visible:
                        item.add_backdrop()
                        item.destroy()
            if len(self.get(DISPLAY_CLASSES, True)) == 0:
                self.groups['Background'] = False
                self.groups['Overlayer'] = True
                self.get(BackgroundX_261).set_value(0)
                self.get(BackgroundY_262).set_value(0)
                self.create_object(OverlayRedux_378, 0, 0) # {'y': 0, 'x': 0, 'create_object': 'OverlayRedux_378'}
                self.groups['Backfix'] = True
        if False:#self.groups['Game']:
            self.set_event_id(542)
            for item in self.get(Strafing2_220, True):
                if item.values.get(4, 0) == 0:
                    item.movement.stop()
            self.set_event_id(543)
            for item in self.get(Strafing2_220, True):
                values = item.values
                if (values.get(4, 0) > 0 and values.get(23, 0) == 0 
                    and values.get(24, 0) == 0):
                    item.movement.movement.start()
                    item.movement.set_speed(9)
            self.set_event_id(544)
            for item in self.get(Strafing2_220, True):
                if item.values.get(23, 0) != 0:
                    self.get(Strafing2_220).set_position(x = immediate_compare(item.values[23], '>', item.x, item.x+1, item.x-1))
                    self.get(Strafing2_220).movement.set_speed(0)
            self.set_event_id(545)
            if select(self.get(Strafing2_220).values.get(24, 0) != 0):
                self.get(Strafing2_220).set_position(y = immediate_compare(self.get(Strafing2_220).values[24], '>', self.get(Strafing2_220).y, self.get(Strafing2_220).y+1, self.get(Strafing2_220).y-1))
                self.get(Strafing2_220).movement.set_speed(0)
            self.set_event_id(546)
            if select(self.get(Strafing2_220).values.get(23, 0) == self.get(Strafing2_220).x):
                self.get(Strafing2_220).values[23] = 0
            self.set_event_id(547)
            if select(self.get(Strafing2_220).values.get(24, 0) == self.get(Strafing2_220).y):
                self.get(Strafing2_220).values[24] = 0
            self.set_event_id(548)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            select(self.get(Strafing_219).values.get(2, 0) > 0) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            self.not_always()):
                self.get(Strafing_219).values[2] = 'self.get(Strafing_219).Speed'
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('202'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(549)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            select(self.get(Strafing_219).values.get(2, 0) == 0) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            self.not_always()):
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
                self.get(Strafing_219).values[2] = 7
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('203'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Strafing_219).GetDirection'))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(550)
            if (select(self.get(Strafing_219).values.get(1, 0) != 'self.get(Strafing_219).GetDirection') and
            select(self.get(Strafing_219).CompareSpeed(0)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('201'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Strafing_219).GetDirection'+self.get(Strafing_219).x*100+self.get(Strafing_219).y*100000))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(551)
            if select(self.get(Fusssoldat_193).values.get(2, 0) >= 8):
                self.get(Fusssoldat_193).values[2] = 0
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('204'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(('self.get(Fusssoldat_193).GetDirection'))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Dir_455).set_value('self.get(Fusssoldat_193).GetDirection')
            self.set_event_id(552)
            if (self.every(1.0) and
            select(self.get(Dir_455).get_value() != 'self.get(Fusssoldat_193).GetDirection') and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1)):
                self.get(Fusssoldat_193).AddToAlterable(2, 1)
            self.set_event_id(553)
            if (PlayerKeyDown(32) and
            self.every(0.01) and
            select(self.get(Fusssoldat_193).values.get(12, 0) > 0) and
            select(negate(self.get(Chat_204).EditIsVisible())) and
            select(self.get(Shop1Blitter_372).ObjectInvisible()) and
            select(self.get(PoliceWin_362).OutsidePlayfield()) and
            select(self.get(TerrorWin_363).OutsidePlayfield())):
                self.get(Counter3_246).add_value(1)
            self.set_event_id(554)
            if (negate(PlayerKeyDown(32)) and
            select(self.get(Counter3_246).get_value() > 0) and
            select(self.get(Fusssoldat_193).values.get(12, 0) == 1) and
            self.not_always()):
                self.create_object(GrenadeSpot_398, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'GrenadeSpot_398'}
                self.get(GrenadeSpot_398).set_visible(False)
                self.get(GrenadeSpot_398).values[3] = 'self.get(Fusssoldat_193).GetDirection'
                self.get(GrenadeSpot_398).values[18] = 5+self.get(Counter3_246).get_value()/5
                self.get(Msg_427).set_value('212'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(GrenadeSpot_398).values[3]+(self.get(GrenadeSpot_398).values[18]-5)*100+self.get(GrenadeSpot_398).x*1000+self.get(GrenadeSpot_398).y*1000000))+str(self.get(Csm_432).get_value()))
                self.get(GrenadeSpot_398).values[1] = 1
                self.get(GrenadeSpot_398).values[2] = self.get(Fusssoldat_193).values[0]
                self.get(Counter3_246).set_value(0)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Active6_214).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(556)
            if (negate(PlayerKeyDown(32)) and
            select(self.get(Counter3_246).get_value() > 0) and
            select(self.get(Fusssoldat_193).values.get(12, 0) == 2) and
            self.not_always()):
                self.create_object(GrenadeSpot_398, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'GrenadeSpot_398'}
                self.get(GrenadeSpot_398).set_visible(False)
                self.get(GrenadeSpot_398).values[3] = 'self.get(Fusssoldat_193).GetDirection'
                self.get(GrenadeSpot_398).values[18] = 5+self.get(Counter3_246).get_value()/5
                self.get(Msg_427).set_value('212'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(((self.get(GrenadeSpot_398).values[3]+32)+(self.get(GrenadeSpot_398).values[18]-5)*100+self.get(GrenadeSpot_398).x*1000+self.get(GrenadeSpot_398).y*1000000))+str(self.get(Csm_432).get_value()))
                self.get(GrenadeSpot_398).values[1] = 2
                self.get(GrenadeSpot_398).values[2] = self.get(Fusssoldat_193).values[0]
                self.get(Counter3_246).set_value(0)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Active6_214).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(558)
            if (negate(PlayerKeyDown(32)) and
            select(self.get(Counter3_246).get_value() > 0) and
            select(self.get(Fusssoldat_193).values.get(12, 0) == 3) and
            self.not_always()):
                self.create_object(C4_374, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 10) # {'y': 10, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'C4_374'}
                self.get(C4_374).values[4] = 4+self.get(Counter3_246).get_value()/3
                self.get(C4_374).values[2] = self.get(Fusssoldat_193).values[0]
                self.get(C4_374).values[9] = 1000+self.get(C4_374).y
                self.get(Msg_427).set_value('212'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(((self.get(C4_374).values[4]+64)+self.get(C4_374).x*100+self.get(C4_374).y*100000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Active6_214).set_visible(False)
                self.get(Counter3_246).set_value(0)
                self.get(C4_374).values[4] = self.get(C4_374).values[4]*50
                self.get(Reclist_426).add_line(str(self.get(C4_374).x)+','+str(self.get(C4_374).y))
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('beep.wav')
            self.set_event_id(559)
            if (negate(PlayerKeyDown(32)) and
            select(self.get(Counter3_246).get_value() > 0) and
            select(self.get(Fusssoldat_193).values.get(12, 0) == 4) and
            self.not_always()):
                self.create_object(GrenadeSpot_398, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'GrenadeSpot_398'}
                self.get(GrenadeSpot_398).set_visible(False)
                self.get(GrenadeSpot_398).values[3] = 'self.get(Fusssoldat_193).GetDirection'
                self.get(GrenadeSpot_398).values[18] = 10+self.get(Counter3_246).get_value()/5
                self.get(Msg_427).set_value('216'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(GrenadeSpot_398).values[3]+(self.get(GrenadeSpot_398).values[18]-10)*100+self.get(GrenadeSpot_398).x*1000+self.get(GrenadeSpot_398).y*1000000))+str(self.get(Csm_432).get_value()))
                self.get(GrenadeSpot_398).values[1] = 4
                self.get(GrenadeSpot_398).values[2] = self.get(Fusssoldat_193).values[0]
                self.get(Counter3_246).set_value(0)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Active6_214).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(561)
            if (negate(PlayerKeyDown(32)) and
            select(self.get(Counter3_246).get_value() > 0) and
            select(self.get(Fusssoldat_193).values.get(12, 0) == 6) and
            self.not_always()):
                self.create_object(GrenadeSpot_398, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'GrenadeSpot_398'}
                self.get(GrenadeSpot_398).set_visible(False)
                self.get(GrenadeSpot_398).values[3] = 'self.get(Fusssoldat_193).GetDirection'
                self.get(GrenadeSpot_398).values[18] = 10+self.get(Counter3_246).get_value()/5
                self.get(Msg_427).set_value('241'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(GrenadeSpot_398).values[3]+(self.get(GrenadeSpot_398).values[18]-10)*100+self.get(GrenadeSpot_398).x*1000+self.get(GrenadeSpot_398).y*1000000))+str(self.get(Csm_432).get_value()))
                self.get(GrenadeSpot_398).values[1] = 6
                self.get(GrenadeSpot_398).values[2] = self.get(Fusssoldat_193).values[0]
                self.get(Counter3_246).set_value(0)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Active6_214).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(565)
            if (negate(PlayerKeyDown(32)) and
            select(self.get(Counter3_246).get_value() > 0) and
            select(self.get(Fusssoldat_193).values.get(12, 0) == 5) and
            self.not_always()):
                self.create_object(GrenadeSpot_398, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'GrenadeSpot_398'}
                self.get(GrenadeSpot_398).set_visible(False)
                self.get(GrenadeSpot_398).values[3] = 'self.get(Fusssoldat_193).GetDirection'
                self.get(GrenadeSpot_398).values[18] = 5+self.get(Counter3_246).get_value()/5
                self.get(Msg_427).set_value('240'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(GrenadeSpot_398).values[3]+(self.get(GrenadeSpot_398).values[18]-5)*100+self.get(GrenadeSpot_398).x*1000+self.get(GrenadeSpot_398).y*1000000))+str(self.get(Csm_432).get_value()))
                self.get(GrenadeSpot_398).values[1] = 5
                self.get(GrenadeSpot_398).values[2] = self.get(Fusssoldat_193).values[0]
                self.get(Counter3_246).set_value(0)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Active6_214).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(580)
            if (select(self.get(Nade_458).values.get(0, 0) >= 100) and
            select(self.get(Nade_458).values.get(1, 0) == 1)):
                self.create_object(Gaswolke_215, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Gaswolke_215'}
                self.get(Gaswolke_215).movement.stop()
                self.get(Gaswolke_215).values[1] = self.get(Nade_458).values[2]
                self.function_gas()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('smoke.wav', self.get(Nade_458).x, self.get(Nade_458).y)
                self.get(Nade_458).destroy()
            self.set_event_id(589)
            if (select(self.get(Nade_458).values.get(0, 0) >= 100) and
            select(self.get(Nade_458).values.get(1, 0) == 2)):
                self.create_object(Exp_247, self.get(Nade_458).x + 0, self.get(Nade_458).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade_458)', 'create_object': 'Exp_247'}
                self.get(Exp_247).values[2] = self.get(Nade_458).values[2]
                self.get(Exp_247).values[9] = 11100000
                self.get(Nade_458).destroy()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('explode.wav', self.get(Nade_458).x, self.get(Nade_458).y)
            self.set_event_id(590)
            if select(self.get(Molotov_450).values.get(0, 0) >= 100):
                self.create_object(P1_452, self.get(Molotov_450).x + 0, self.get(Molotov_450).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Molotov_450)', 'create_object': 'P1_452'}
                self.get(P1_452).values[2] = self.get(Molotov_450).values[2]
                self.get(P1_452).values[9] = self.get(P1_452).y*1000
                self.get(P1_452).values[18] = 200
                self.get(P1_452).values[19] = 1
                self.get(P1_452).values[20] = 4
                self.get(P1_452).values[22] = 20
                self.get(P1_452).values[1] = self.get(Molotov_450).values[2]
                self.create_object(BigflameDmg_457, self.get(P1_452).x + 0, self.get(P1_452).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'BigflameDmg_457'}
                self.get(BigflameDmg_457).values[2] = self.get(P1_452).values[2]
                self.get(BigflameDmg_457).set_visible(False)
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('explode.wav', self.get(Molotov_450).x, self.get(Molotov_450).y)
                self.get(Molotov_450).destroy()
            self.set_event_id(591)
            if select(self.get(Active17_451).values.get(0, 0) >= 380):
                self.create_object(Explode_453, self.get(Active17_451).x + 0, self.get(Active17_451).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Active17_451)', 'create_object': 'Explode_453'}
                self.get(Explode_453).values[9] = 11100000
                self.get(Active17_451).destroy()
            self.set_event_id(592)
            if select(self.get(FlameDmg_456).values.get(0, 0) >= 380):
                self.get(FlameDmg_456).destroy()
            self.set_event_id(593)
            if select(self.get(P1_452).values.get(0, 0) >= 650):
                self.create_object(Explode_453, self.get(P1_452).x + 0, self.get(P1_452).x + -10) # {'y': -10, 'x': 0, 'parent': 'self.get(P1_452)', 'create_object': 'Explode_453'}
                self.get(Explode_453).values[9] = 11100000
                self.get(P1_452).destroy()
            self.set_event_id(594)
            if select(self.get(BigflameDmg_457).values.get(0, 0) >= 650):
                self.get(BigflameDmg_457).destroy()
            self.set_event_id(595)
            if (select(self.get(P1_452).values.get(18, 0) <= 0) and
            select(self.get(P1_452).values.get(19, 0) >= 1)):
                self.get(P1_452).values[19] -= 1
                self.get(P1_452).values[18] = 200
                self.get(P1_452).values[20] = 4
                self.get(P1_452).values[22] = 20
            self.set_event_id(596)
            if (select(self.get(P1_452).values.get(20, 0) > 0) and
            select(self.get(P1_452).values.get(22, 0) <= 0)):
                self.function_fire(self.get(P1_452).values[2])
            self.set_event_id(605)
            if self.every(0.02):
                self.get(P1_452).values[18] -= 1
                self.get(P1_452).values[22] -= 1
            self.set_event_id(607)
            if (select(self.get(Nade2_459).CompareSpeed(0)) and
            select(self.get(Nade2_459).values.get(23, 0) == 1)):
                self.get(Nade2_459).force_animation('User defined 2')
            self.set_event_id(608)
            if (select(self.get(Nade2_459).CompareSpeed(0)) and
            select(self.get(Nade2_459).values.get(23, 0) == 1)):
                self.get(Nade2_459).force_animation('User defined 1')
            self.set_event_id(609)
            if (select(self.get(Nade2_459).CompareSpeed(0)) and
            select(self.get(Nade2_459).values.get(23, 0) == 2)):
                self.get(Nade2_459).force_animation('User defined 4')
            self.set_event_id(610)
            if (select(self.get(Nade2_459).CompareSpeed(0)) and
            select(self.get(Nade2_459).values.get(23, 0) == 2)):
                self.get(Nade2_459).force_animation('User defined 3')
            self.set_event_id(611)
            if (select(self.get(Nade2_459).values.get(0, 0) >= 190) and
            select(self.get(Nade2_459).values.get(23, 0) == 1)):
                self.create_object(Flashbang2_379, self.get(Nade2_459).x + 0, self.get(Nade2_459).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade2_459)', 'create_object': 'Flashbang2_379'}
                self.get(Flashbang2_379).values[9] = self.get(Flashbang2_379).y*1000
                self.create_object(Flash_380, self.get(Nade2_459).x + 0, self.get(Nade2_459).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade2_459)', 'create_object': 'Flash_380'}
                self.get(Flash_380).values[23] = self.get(Strafing_219).x-self.get(Flash_380).x
                self.get(Flash_380).values[24] = self.get(Strafing_219).y-self.get(Flash_380).y
                self.get(Flash_380).values[21] = self.get(Flash_380).values[23]/abs(self.get(Flash_380).values[23])
                self.get(Flash_380).values[22] = self.get(Flash_380).values[24]/abs(self.get(Flash_380).values[24])
                self.get(Flash_380).values[1] = 550
                self.get(Nade2_459).destroy()
                for loop_index in xrange((max(abs(self.get(Flash_380).values[23]), abs(self.get(Flash_380).values[24]))+1)):
                    if self.loop_flash(loop_index) == False: break
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('smoke.wav', self.get(Nade2_459).x, self.get(Nade2_459).y)
            self.set_event_id(612)
            if (select(self.get(Nade2_459).values.get(0, 0) >= 190) and
            select(self.get(Nade2_459).values.get(23, 0) == 2)):
                self.create_object(SmokeExp_460, self.get(Nade2_459).x + 0, self.get(Nade2_459).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade2_459)', 'create_object': 'SmokeExp_460'}
                self.get(SmokeExp_460).values[9] = 9999000+self.get(SmokeExp_460).x
                self.get(SmokeExp_460).set_direction(0)
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('smoke.wav', self.get(Nade2_459).x, self.get(Nade2_459).y)
            self.set_event_id(613)
            if (select(self.get(Nade2_459).values.get(0, 0) >= 190) and
            select(self.get(Nade2_459).values.get(23, 0) == 2)):
                self.create_object(SmokeExp_460, self.get(Nade2_459).x + 0, self.get(Nade2_459).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Nade2_459)', 'create_object': 'SmokeExp_460'}
                self.get(SmokeExp_460).values[9] = 9999000+self.get(SmokeExp_460).x
                self.get(SmokeExp_460).set_direction(16)
                self.get(Nade2_459).destroy()
            self.set_event_id(615)
            if select(self.get(Fusssoldat2_194).IsOverlapping(SmokeExp_460)):
                self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
                for loop_index in xrange('self.get(Fusssoldat2_194).ObjectCount'):
                    if self.loop_testhide(loop_index) == False: break
            self.set_event_id(617)
            if select(self.get(NameTag2_429).values.get(23, 0) > 0):
                self.get(NameTag2_429).values[23] -= 1
            self.set_event_id(618)
            if select(self.get(NameTag3_433).values.get(23, 0) > 0):
                self.get(NameTag3_433).values[23] -= 1
            self.set_event_id(619)
            if select(self.get(NameTag2_429).values.get(23, 0) == 0):
                self.get(NameTag2_429).set_visible(True)
            self.set_event_id(620)
            if select(self.get(NameTag3_433).values.get(23, 0) == 0):
                self.get(NameTag3_433).set_visible(True)
            self.set_event_id(621)
            if select(self.get(Gaswolke_215).values.get(0, 0) >= 35):
                self.get(Gaswolke_215).destroy()
            self.set_event_id(622)
            if (self.every(1.0) and
            select(self.get(Respawn_201).visible)):
                self.get(Respawn_201).subtract_value(1)
            self.set_event_id(623)
            if (select(self.get(Respawn_201).get_value() == 0) and
            self.get_global_value(2) == 0 and
            self.not_always()):
                self.get(String2_200).set_visible(False)
                self.get(Respawn_201).set_visible(False)
                self.get(Respawn_201).set_value(5)
                self.get(Respawntext_392).set_visible(True)
            self.set_event_id(624)
            if (Qt.Key_Space in self.scene.key_presses and
            select(self.get(Respawntext_392).visible) and
            self.get_global_value(2) == 0 and
            self.get_global_value(1) == 0 and
            select(self.get(DM_412).get_value() == 1) and
            negate(self.groups['Chat'])):
                self.get(Msg_427).set_value('110'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
                self.function_sendall()
                self.get(PingCounter_232).set_value(0)
                self.get(Respawntext_392).set_visible(False)
            self.set_event_id(643)
            if select(self.get(Splitter_202).values.get(0, 0) >= 8):
                self.get(Splitter_202).destroy()
            self.set_event_id(644)
            if (Qt.Key_Return in self.scene.key_presses and
            negate(self.groups['Chat'])):
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeVisible()
                self.get(Chat_204).set_focus(True)
                self.get(Fusssoldat_193).values[23] = 1
                self.get(Fusssoldat_193).values[7] = 0
                self.players[0].set_ignore(True)
                self.get(ChattingPlayer_356).values[1] = 1
                self.get(Strafing_219).movement.stop()
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('225'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.groups['Chat'] = True
            self.set_event_id(645)
            if self.every(0.5):
                self.get(Fusssoldat_193).values[22] += 1
                self.get(qualifier_8).AddToAlterable(0, 1)
            self.set_event_id(646)
            if (self.every(1.0) and
            select(self.get(Fusssoldat_193).values.get(22, 0) >= 25) and
            select(self.get(DurchlaufChat_245).get_value() == 0)):
                self.get(Fusssoldat_193).values[22] = 0
                self.get(Message1_205).set_value('')
                self.get(DurchlaufChat_245).set_value(1)
            self.set_event_id(647)
            if (self.every(1.0) and
            select(self.get(Fusssoldat_193).values.get(22, 0) >= 25) and
            select(self.get(DurchlaufChat_245).get_value() == 1)):
                self.get(Fusssoldat_193).values[22] = 0
                self.get(Message1_205).set_value('')
                self.get(Message2_206).set_value('')
                self.get(DurchlaufChat_245).set_value(2)
            self.set_event_id(648)
            if (self.every(1.0) and
            select(self.get(Fusssoldat_193).values.get(22, 0) >= 25) and
            select(self.get(DurchlaufChat_245).get_value() == 2)):
                self.get(Fusssoldat_193).values[22] = 0
                self.get(Message1_205).set_value('')
                self.get(Message2_206).set_value('')
                self.get(Message3_207).set_value('')
                self.get(DurchlaufChat_245).set_value(3)
            self.set_event_id(649)
            if (self.every(1.0) and
            select(self.get(Fusssoldat_193).values.get(22, 0) >= 25) and
            select(self.get(DurchlaufChat_245).get_value() == 3)):
                self.get(Fusssoldat_193).values[22] = 0
                self.get(Message1_205).set_value('')
                self.get(Message2_206).set_value('')
                self.get(Message3_207).set_value('')
                self.get(Message4_243).set_value('')
                self.get(DurchlaufChat_245).set_value(0)
            self.set_event_id(650)
            if select(self.get(qualifier_8).values.get(0, 0) >= 50):
                self.get(qualifier_8).destroy()
            self.set_event_id(651)
            if select(self.get(qualifier_8).values.get(6, 0) > 0):
                self.get(qualifier_8).values[6] -= 1
                self.create_object(Blood3_253, self.get(qualifier_8).x + 0, self.get(qualifier_8).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(qualifier_8)', 'create_object': 'Blood3_253'}
                self.get(Blood3_253).values[0] = -5+randrange(6)
                self.get(Blood3_253).values[1] = randrange(7)-3
                self.get(Blood3_253).values[9] = 999887
            self.set_event_id(664)
            if (select(self.get(AmmoCurrent_311).get_value() == 0) and
            self.players[0].lives == 1 and
            negate(self.groups['Reload'])):
                self.groups['Reload'] = True
                SoundAutoPlay('reload.wav')
            self.set_event_id(665)
            if (select(self.get(AmmoCurrent_311).get_value() == 0) and
            self.players[0].lives == 8 and
            negate(self.groups['Reload'])):
                self.groups['Reload'] = True
                SoundAutoPlay('reload.wav')
            self.set_event_id(666)
            if (select(self.get(AmmoCurrent_311).get_value() == 0) and
            self.players[0].lives != 1 and
            self.players[0].lives != 8 and
            select(self.get(AmmoFull_312).get_value() > 0) and
            negate(self.groups['Reload'])):
                self.groups['Reload'] = True
                SoundAutoPlay('reload.wav')
            self.set_event_id(681)
            if select(self.get(SkillCounter_211).get_value() == 3):
                self.get(SkillCounter_211).set_value(4)
                self.create_object(Frantic_248, 900, 300) # {'y': 300, 'x': 900, 'create_object': 'Frantic_248'}
                PlaySample(discreturn)
                self.get(Frantic_248).values[9] = 33000000
            self.set_event_id(682)
            if select(self.get(SkillCounter_211).get_value() == 7):
                self.get(SkillCounter_211).set_value(8)
                self.create_object(Daunting_249, -200, 300) # {'y': 300, 'x': -200, 'create_object': 'Daunting_249'}
                PlaySample(discreturn)
                self.get(Daunting_249).values[9] = 33000000
            self.set_event_id(683)
            if select(self.get(SkillCounter_211).get_value() == 10):
                self.get(SkillCounter_211).set_value(13)
                self.create_object(Godlike_250, 400, -75) # {'y': -75, 'x': 400, 'create_object': 'Godlike_250'}
                PlaySample(scream2)
                self.get(Godlike_250).values[9] = 33000000
            self.set_event_id(687)
            if self.every(1.0):
                AddGlobalValue(3, 1)
                self.get(InvincibleTime_388).subtract_value(1)
            self.set_event_id(689)
            if True:
                self.get(Fusssoldat_193).set_position(self.get(Strafing_219).x + 0, self.get(Strafing_219).x + -10) # {'y': -10, 'x': 0, 'parent': 'self.get(Strafing_219)'}
                self.get(Fusssoldat_193).LookAt({'y': 0, 'x': 0, 'parent': 'self.get(Active9_222)'})
                self.get(Counter3_246).set_position(self.get(Fusssoldat_193).x + -10, self.get(Fusssoldat_193).x + 24) # {'y': 24, 'x': -10, 'parent': 'self.get(Fusssoldat_193)'}
                self.get(Sleep_324).subtract_value(1)
                self.get(NameTag2_429).set_position(self.get(Fusssoldat2_194).x + -73, self.get(Fusssoldat2_194).x + -25) # {'y': -25, 'x': -73, 'parent': 'self.get(Fusssoldat2_194)'}
                self.get(NameTag3_433).set_position(self.get(Fusssoldat2_194).x + -75, self.get(Fusssoldat2_194).x + -27) # {'y': -27, 'x': -75, 'parent': 'self.get(Fusssoldat2_194)'}
                self.get(Snipercounter_438).set_position(self.get(Fusssoldat_193).x + -10, self.get(Fusssoldat_193).x + 27) # {'y': 27, 'x': -10, 'parent': 'self.get(Fusssoldat_193)'}
                self.get(Chatting_355).set_position(self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + -15) # {'y': -15, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)'}
            self.set_event_id(690)
            if (self.every(0.3) and
            select(self.get(Strafing_219).CompareSpeed(0)) and
            self.players[0].lives != 5 and
            self.players[0].lives != 12 and
            self.not_always()):
                self.get(Accuracy_238).SetMinimumValue(8)
            self.set_event_id(691)
            if (self.every(0.3) and
            select(self.get(Strafing_219).CompareSpeed(0)) and
            self.players[0].lives == 5 and
            self.not_always()):
                self.get(Accuracy_238).SetMinimumValue(30)
            self.set_event_id(692)
            if (self.every(0.3) and
            select(self.get(Strafing_219).CompareSpeed(0)) and
            self.players[0].lives == 12 and
            self.not_always()):
                self.get(Accuracy_238).SetMinimumValue(15)
            self.set_event_id(693)
            if (self.every(0.08) and
            select(self.get(Strafing_219).CompareSpeed(0)) and
            select(self.get(Accuracy_238).get_value() > 10)):
                self.get(Accuracy_238).subtract_value(3)
            self.set_event_id(694)
            if (self.every(0.08) and
            select(self.get(Strafing_219).CompareSpeed(0)) and
            self.players[0].lives != 5):
                self.get(Accuracy_238).SetMinimumValue(0)
                self.get(Accuracy_238).subtract_value(3)
            self.set_event_id(695)
            if (self.every(0.08) and
            select(self.get(Strafing_219).CompareSpeed(0)) and
            self.players[0].lives == 5 and
            negate(PlayerKeyDown(16))):
                self.get(Accuracy_238).SetMinimumValue(22)
                self.get(Accuracy_238).subtract_value(3)
            self.set_event_id(696)
            if self.get(Head_441).values[0] == self.get(Fusssoldat2_194).values[0]:
                self.get(Head_441).set_position(self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + -6) # {'y': -6, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)'}
                self.get(Head_441).set_direction('self.get(Fusssoldat2_194).GetDirection')
            self.set_event_id(697)
            if self.get(Strafing2_220).values[0] == self.get(Fusssoldat2_194).values[0]:
                self.get(Fusssoldat2_194).set_position(self.get(Strafing2_220).x + 0, self.get(Strafing2_220).x + -10) # {'y': -10, 'x': 0, 'parent': 'self.get(Strafing2_220)'}
                self.get(Fusssoldat2_194).values[4] = self.get(Strafing2_220).values[4]
            self.set_event_id(698)
            if (select(self.get(Fusssoldat2_194).values.get(18, 0) == 0) and
            select(self.get(Fusssoldat2_194).values.get(4, 0) <= 2)):
                self.get(Fusssoldat2_194).force_animation('Stopped')
            self.set_event_id(699)
            if (select(self.get(Fusssoldat2_194).values.get(18, 0) == 0) and
            select(self.get(Fusssoldat2_194).values.get(4, 0) > 3)):
                self.get(Fusssoldat2_194).force_animation('Walking')
            self.set_event_id(700)
            if (select(self.get(Fusssoldat2_194).values.get(18, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(4, 0) <= 2)):
                self.get(Fusssoldat2_194).force_animation('User defined 2')
            self.set_event_id(701)
            if (select(self.get(Fusssoldat2_194).values.get(18, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(4, 0) > 3)):
                self.get(Fusssoldat2_194).force_animation('User defined 1')
            self.set_event_id(702)
            if (select(self.get(Fusssoldat2_194).values.get(18, 0) == 2) and
            select(self.get(Fusssoldat2_194).values.get(4, 0) <= 2)):
                self.get(Fusssoldat2_194).force_animation('User defined 4')
            self.set_event_id(703)
            if (select(self.get(Fusssoldat2_194).values.get(18, 0) == 2) and
            select(self.get(Fusssoldat2_194).values.get(4, 0) > 3)):
                self.get(Fusssoldat2_194).force_animation('User defined 3')
            self.set_event_id(704)
            if select(self.get(Fusssoldat2_194).values.get(22, 0) == 1):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat2_194).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat2_194)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.get(Fusssoldat2_194).values[22] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
            self.set_event_id(705)
            if select(self.get(Fusssoldat2_194).values.get(22, 0) == 2):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat2_194).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat2_194)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.get(Fusssoldat2_194).values[22] = 0
                self.get(Rauch_197).force_animation('User defined 1')
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
            self.set_event_id(706)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 0) and
            select(self.get(Strafing_219).CompareSpeed(0))):
                self.get(Fusssoldat_193).force_animation('Stopped')
            self.set_event_id(707)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 0) and
            select(self.get(Strafing_219).CompareSpeed(0))):
                self.get(Fusssoldat_193).force_animation('Walking')
            self.set_event_id(708)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
            select(self.get(Strafing_219).CompareSpeed(0))):
                self.get(Fusssoldat_193).force_animation('User defined 1')
            self.set_event_id(709)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
            select(self.get(Strafing_219).CompareSpeed(0))):
                self.get(Fusssoldat_193).force_animation('User defined 2')
            self.set_event_id(710)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
            select(self.get(Strafing_219).CompareSpeed(0))):
                self.get(Fusssoldat_193).force_animation('User defined 4')
            self.set_event_id(711)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
            select(self.get(Strafing_219).CompareSpeed(0))):
                self.get(Fusssoldat_193).force_animation('User defined 3')
            self.set_event_id(712)
            if (negate(Qt.Key_Tab in self.scene.key_downs) and
            negate(self.groups['Map change']) and
            self.not_always()):
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
                self.get(Player_334).set_position(5, 634) # {'y': 634, 'x': 5}
            self.set_event_id(713)
            if (Qt.Key_Tab in self.scene.key_presses and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
            self.set_event_id(714)
            if (Qt.Key_Tab in self.scene.key_downs and
            negate(self.groups['Map change']) and
            self.not_always()):
                self.get(ScoreBoard_231).add_line(str(self.get(Frags_209).get_value())+','+self.get(RealName_390).text+','+str(self.get(VisibleId_424).get_value())+','+str(self.get(Ping_233).get_value())+','+str(self.get(Deaths_210).get_value())+',1')
                self.get(ScoreBar_234).set_visible(True)
                self.get(NameScore_235).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore_236).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore_237).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing_307).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore2_347).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore3_351).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore2_348).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore3_352).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore2_349).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore3_353).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing2_350).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing3_354).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(PlOnlineText_316).set_visible(True)
                self.get(Players_317).set_visible(True)
                for loop_index in xrange('self.get(Fusssoldat2_194).ObjectCount'):
                    if self.loop_entry(loop_index) == False: break
                for loop_index in xrange('self.get(ScoreBoard_231).ListGetLineCount'):
                    if self.loop_list(loop_index) == False: break
            self.set_event_id(731)
            if True:
                self.get(Oben_239).set_position(x = self.get(Active9_222).x)
                self.get(Rechts_241).set_position(y = self.get(Active9_222).y)
                self.get(Links_242).set_position(y = self.get(Active9_222).y)
                self.get(Oben_239).set_position(y = self.get(Active9_222).y-self.get(Accuracy_238).get_value())
                self.get(Unten_240).set_position(x = self.get(Active9_222).x)
                self.get(Unten_240).set_position(y = self.get(Active9_222).y+self.get(Accuracy_238).get_value())
                self.get(Rechts_241).set_position(x = self.get(Active9_222).x+self.get(Accuracy_238).get_value())
                self.get(Links_242).set_position(x = self.get(Active9_222).x-self.get(Accuracy_238).get_value())
            self.set_event_id(732)
            if self.every(0.04):
                self.get(Blood3_253).set_position(x = self.get(Blood3_253).x+self.get(Blood3_253).values[1])
                self.get(Blood3_253).set_position(y = self.get(Blood3_253).y+self.get(Blood3_253).values[0])
                self.get(Blood3_253).AddToAlterable(0, 1)
                self.get(Blood3_253).AddToAlterable(2, 1)
            self.set_event_id(733)
            if select(self.get(Fusssoldat2_194).values.get(6, 0) > 0):
                self.create_object(Blood3_253, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Blood3_253'}
                self.get(Blood3_253).values[0] = -5+randrange(6)
                self.get(Blood3_253).values[1] = randrange(7)-3
                self.get(Blood3_253).values[9] = 999887
                self.get(Fusssoldat2_194).values[6] -= 1
            self.set_event_id(734)
            if select(self.get(Fusssoldat2_194).values.get(6, 0) < 0):
                self.create_object(Blood3_253, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + -7) # {'y': -7, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Blood3_253'}
                self.get(Blood3_253).values[0] = -5+randrange(6)
                self.get(Blood3_253).values[1] = randrange(7)-3
                self.get(Blood3_253).values[9] = 999887
                self.get(Fusssoldat2_194).AddToAlterable(6, 1)
            self.set_event_id(735)
            if select(self.get(Fusssoldat_193).values.get(6, 0) > 0):
                self.create_object(Blood3_253, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Blood3_253'}
                self.get(Blood3_253).values[0] = -5+randrange(6)
                self.get(Blood3_253).values[1] = randrange(7)-3
                self.get(Blood3_253).values[9] = 999887
                self.get(Fusssoldat_193).values[6] -= 1
            self.set_event_id(736)
            if select(self.get(Fusssoldat_193).values.get(6, 0) < 0):
                self.create_object(Blood3_253, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + -7) # {'y': -7, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Blood3_253'}
                self.get(Blood3_253).values[0] = -5+randrange(6)
                self.get(Blood3_253).values[1] = randrange(7)-3
                self.get(Blood3_253).values[9] = 999887
                self.get(Fusssoldat_193).AddToAlterable(6, 1)
            self.set_event_id(737)
            if select(self.get(Blood3_253).values.get(2, 0) > 10):
                self.get(Blood3_253).destroy()
            self.set_event_id(738)
            if self.every(0.06):
                self.get(Active2_254).AddToAlterable(0, 1)
            self.set_event_id(740)
            if select(self.get(Active2_254).values.get(0, 0) > 1):
                self.get(Active2_254).movement.stop()
            self.set_event_id(741)
            if select(self.get(Active2_254).values.get(0, 0) > 300):
                self.get(Active2_254).destroy()
            self.set_event_id(742)
            if select(self.get(Chatting_355).values.get(1, 0) == 1):
                self.get(Chatting_355).set_visible(True)
            self.set_event_id(743)
            if select(self.get(Chatting_355).values.get(1, 0) == 0):
                self.get(Chatting_355).set_visible(False)
            self.set_event_id(770)
            if select(self.get(C4_374).values.get(4, 0) <= 0):
                self.create_object(Exp_247, self.get(C4_374).x + -50, self.get(C4_374).x + 0) # {'y': 0, 'x': -50, 'parent': 'self.get(C4_374)', 'create_object': 'Exp_247'}
                self.create_object(Exp_247, self.get(C4_374).x + 50, self.get(C4_374).x + 0) # {'y': 0, 'x': 50, 'parent': 'self.get(C4_374)', 'create_object': 'Exp_247'}
                self.create_object(Exp_247, self.get(C4_374).x + 0, self.get(C4_374).x + -50) # {'y': -50, 'x': 0, 'parent': 'self.get(C4_374)', 'create_object': 'Exp_247'}
                self.create_object(Exp_247, self.get(C4_374).x + 0, self.get(C4_374).x + 50) # {'y': 50, 'x': 0, 'parent': 'self.get(C4_374)', 'create_object': 'Exp_247'}
                self.create_object(Exp_247, self.get(C4_374).x + 0, self.get(C4_374).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(C4_374)', 'create_object': 'Exp_247'}
                self.get(Exp_247).values[2] = self.get(C4_374).values[2]
                self.create_object(Destroy_375, self.get(C4_374).x + 0, self.get(C4_374).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(C4_374)', 'create_object': 'Destroy_375'}
                self.get(Destroy_375).set_visible(False)
                self.get(Exp_247).values[9] = 11100000
                self.get(C4_374).destroy()
                SoundAutoPlay('explode.wav')
            self.set_event_id(785)
            if self.every(0.01):
                self.get(Rauch_197).AddToAlterable(0, 1)
                self.get(Nade_458).AddToAlterable(0, 1)
                self.get(ShotLatence_230).subtract_value(1)
                self.get(PingCounter_232).add_value(2)
                self.get(ActiveObject1_218).values[9] = 2
                self.get(C4_374).values[4] -= 1
                self.get(Nade2_459).AddToAlterable(0, 1)
                self.get(Splitter_202).set_position(x = self.get(Splitter_202).x+self.get(Splitter_202).values[1])
                self.get(Splitter_202).set_position(y = self.get(Splitter_202).y+self.get(Splitter_202).values[0])
                self.get(Splitter_202).AddToAlterable(0, 1)
                self.get(Splitter_202).AddToAlterable(2, 1)
                self.get(Molotov_450).AddToAlterable(0, 1)
                self.get(Active17_451).AddToAlterable(0, 1)
                self.get(P1_452).AddToAlterable(0, 1)
                self.get(FlameDmg_456).AddToAlterable(0, 1)
                self.get(BigflameDmg_457).AddToAlterable(0, 1)
            self.set_event_id(786)
            if select(self.get(Rauch_197).values.get(0, 0) >= 5):
                self.get(Rauch_197).destroy()
            self.set_event_id(788)
            if (self.every(2.0) and
            select(self.get(ScoreBar_234).visible) and
            select(self.get(Respawn_201).get_value() <= 10) and
            negate(self.groups['Map change'])):
                self.get(ScoreBoard_231).reset()
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Player_334).set_position(5, 634) # {'y': 634, 'x': 5}
                self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
                self.get(Strafing_219).flags[10] = True
            self.set_event_id(789)
            if select(self.get(Strafing_219).flags[10] == True):
                self.get(ScoreBoard_231).add_line(str(self.get(Frags_209).get_value())+','+self.get(RealName_390).text+','+str(self.get(VisibleId_424).get_value())+','+str(self.get(Ping_233).get_value())+','+str(self.get(Deaths_210).get_value())+',1')
                self.get(ScoreBar_234).set_visible(True)
                self.get(NameScore_235).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore_236).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore_237).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing_307).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore2_347).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore3_351).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore2_348).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore3_352).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore2_349).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore3_353).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing2_350).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing3_354).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(PlOnlineText_316).set_visible(True)
                self.get(Players_317).set_visible(True)
                self.get(Strafing_219).flags[10] = False
                for loop_index in xrange('self.get(Fusssoldat2_194).ObjectCount'):
                    if self.loop_entry(loop_index) == False: break
                for loop_index in xrange('self.get(ScoreBoard_231).ListGetLineCount'):
                    if self.loop_list(loop_index) == False: break
            self.set_event_id(790)
            if select(self.get(Strafing2_220).OutsidePlayfield()):
                self.get(Strafing2_220).movement.stop()
                self.get(Strafing2_220).values[4] = 0
            self.set_event_id(791)
            if select(self.get(Strafing2_220).values.get(25, 0) == 0):
                self.get(Strafing2_220).values[23] = 0
                self.get(Strafing2_220).values[24] = 0
                self.get(Strafing2_220).values[4] = 0
            self.set_event_id(792)
            if select(self.get(Counter_434).get_value() > self.get(Fusssoldat_193).values[5]):
                self.get(Counter_434).subtract_value(immediate_compare((self.get(Counter_434).get_value()-self.get(Fusssoldat_193).values[5]), '>', 1, 2, 1))
            self.set_event_id(793)
            if select(self.get(Counter_434).get_value() < self.get(Fusssoldat_193).values[5]):
                self.get(Counter_434).add_value(immediate_compare(self.get(Fusssoldat_193).values[5]-(self.get(Counter_434).get_value()), '>', 1, 2, 1))
            self.set_event_id(794)
            if True:
                self.get(Counter2_439).set_value(self.get(Counter_434).get_value())
                self.get(Counter4_440).set_value(self.get(Counter_434).get_value())
            self.set_event_id(795)
            if select(self.get(Counter_434).get_value() > 70):
                self.get(Counter_434).set_visible(True)
                self.get(Counter2_439).set_visible(False)
                self.get(Counter4_440).set_visible(False)
            self.set_event_id(796)
            if (select(self.get(Counter_434).get_value() <= 70) and
            select(self.get(Counter_434).get_value() > 35)):
                self.get(Counter2_439).set_visible(True)
                self.get(Counter_434).set_visible(False)
                self.get(Counter4_440).set_visible(False)
            self.set_event_id(797)
            if select(self.get(Counter_434).get_value() <= 35):
                self.get(Counter4_440).set_visible(True)
                self.get(Counter2_439).set_visible(False)
                self.get(Counter_434).set_visible(False)
            self.set_event_id(798)
            if select(self.get(Active2_254).MovementStopped()):
                self.get(Active2_254).values[9] = (self.get(Active2_254).y*1000+self.get(Active2_254).x)*-1
            self.set_event_id(800)
            if select(self.get(Active9_222).values.get(7, 0) == 2):
                self.get(Active9_222).values[7] = 0
                self.get(Oben_239).restore_animation()
                self.get(Unten_240).restore_animation()
                self.get(Rechts_241).restore_animation()
                self.get(Links_242).restore_animation()
            self.set_event_id(803)
            if select(self.get(Fusssoldat_193).values.get(14, 0) == 1):
                self.get(Follower_442).set_position(self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)'}
        if False:#self.groups['Client']:
            self.set_event_id(806)
            if (self.every(30.0) and
            False):
                self.function_shc()
            self.set_event_id(807)
            if (self.every(25.0) and
            select(self.get(Money_366).get_value() != to_number(self.get(String31_437).text)) and
            False):
                self.get(ServerError_60).set_value('Money cheat detected!')
                self.set_frame(4)
            self.set_event_id(809)
            if (self.get_global_value(3) >= 40 and
            self.get_global_value(1) == 0):
                self.get(ErrorMsg_244).set_value('Bad connection or server closed')
                self.groups['Disconnect'] = True
            self.set_event_id(810)
            if (self.get_global_value(3) >= 20 and
            select(self.get(Strafing_219).flags[9] == False)):
                self.groups['Custom Movement'] = False
                self.get(Strafing_219).movement.stop()
                self.get(Strafing_219).flags[9] = True
                self.get(ChangeMap_217).set_value('Connection interrupted...')
                self.get(ChangeMap_217).set_visible(True)
            self.set_event_id(811)
            if (select(self.get(Fusssoldat2_194).values.get(19, 0) > 0) and
            select(self.get(Strafing_219).values.get(5, 0) > 2)):
                self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[19]+self.get(Fusssoldat2_194).values[12]*1000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat2_194).values[6] = immediate_compare(self.get(Fusssoldat2_194).values[19], '<', 300, self.get(Fusssoldat2_194).values[19]/5, ((self.get(Fusssoldat2_194).values[19]-300)/5)*-1)
                self.get(Fusssoldat2_194).values[19] -= immediate_compare(self.get(Fusssoldat2_194).values[19], '<', 300, 0, 300)
                self.get(Fusssoldat2_194).values[24] -= self.get(Fusssoldat2_194).values[19]
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[5] = 1
                self.get(Fusssoldat2_194).values[19] = 0
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
                return False
            self.set_event_id(812)
            if (select(self.get(Fusssoldat_193).IsOverlapping(Gaswolke_215)) and
            self.every(0.1) and
            select(self.get(Fusssoldat_193).values.get(0, 0) == self.get(Gaswolke_215).values[1])):
                self.get(Fusssoldat_193).AddToAlterable(15, 2+randrange(3))
            self.set_event_id(813)
            if select(self.get(Fusssoldat_193).values.get(15, 0) >= 25):
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[15]+self.get(VisibleId_424).get_value()*1000+100000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[15]
                self.get(Fusssoldat_193).values[6] = 10
                self.get(Fusssoldat_193).values[15] = 0
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
            self.set_event_id(814)
            if (select(self.get(Fusssoldat2_194).IsOverlapping(Gaswolke_215)) and
            self.every(0.1) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(Gaswolke_215).values.get(1, 0) == self.get(Fusssoldat_193).values[0])):
                self.get(Fusssoldat2_194).AddToAlterable(15, 2+randrange(3))
            self.set_event_id(815)
            if (select(self.get(Fusssoldat2_194).values.get(15, 0) >= 25) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
                self.get(Fusssoldat2_194).values[24] -= self.get(Fusssoldat2_194).values[15]
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[15]+self.get(Fusssoldat2_194).values[12]*1000+100000))+str(self.get(Csm_432).get_value()))
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[5] = 1
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
        if False:#self.groups['Overlayer']:
            self.set_event_id(824)
            if True:
                self.get(Fusssoldat_193).values[9] = self.get(Fusssoldat_193).y*1000
                self.get(Fusssoldat2_194).values[9] = self.get(Fusssoldat2_194).y*1000
                self.get(Strafing_219).values[9] = self.get(Strafing_219).y*1000
                self.get(Strafing2_220).values[9] = self.get(Strafing2_220).y*1000
                self.get(qualifier_2).values[2] = 0
                self.get(Nade2_459).values[9] = self.get(Nade2_459).y*1000
                self.get(PlShadow_382).set_position(self.get(Fusssoldat_193).x + -7, self.get(Fusssoldat_193).x + 5) # {'y': 5, 'x': -7, 'parent': 'self.get(Fusssoldat_193)'}
                self.get(PlShadow_382).values[9] = self.get(Fusssoldat_193).y*1000-1
                self.get(PlShadow_382).set_direction('self.get(Fusssoldat_193).GetDirection')
                self.get(PlShadow2_383).values[9] = self.get(Fusssoldat2_194).y*1000-1
                self.get(PlShadow2_383).set_direction('self.get(Fusssoldat2_194).GetDirection')
                self.get(PlShadow2_383).set_position(self.get(Fusssoldat2_194).x + -7, self.get(Fusssoldat2_194).x + 5) # {'y': 5, 'x': -7, 'parent': 'self.get(Fusssoldat2_194)'}
                self.get(Gaswolke_215).values[9] = self.get(Gaswolke_215).x+self.get(Gaswolke_215).y*1000+1000000
                self.get(Active17_451).values[9] = self.get(Active17_451).y*1000
                self.get(P1_452).values[9] = self.get(P1_452).y*1000
                self.get(FlameDmg_456).values[9] = self.get(FlameDmg_456).y*1000
            self.set_event_id(825)
            if self.every(0.25):
                self.get(Gaswolke_215).AddToAlterable(0, 1)
                self.groups['Layer'] = True
            self.set_event_id(826)
            if (select(self.get(Strafing2_220).IsOverlapping(qualifier_2)) and
            select(self.get(qualifier_2).values.get(14, 0) == 0)):
                self.get(qualifier_2).values[2] = 1
            self.set_event_id(827)
            if (select(self.get(Strafing_219).IsOverlapping(qualifier_2)) and
            select(self.get(qualifier_2).values.get(14, 0) == 0)):
                self.get(qualifier_2).values[2] = 1
            self.set_event_id(828)
            if select(self.get(C4_374).IsOverlapping(qualifier_2)):
                self.get(qualifier_2).values[2] = 1
            self.set_event_id(829)
            if select(self.get(Nade2_459).IsOverlapping(qualifier_2)):
                self.get(qualifier_2).values[2] = 1
            self.set_event_id(830)
            if (select(self.get(qualifier_2).values.get(2, 0) == 1) and
            self.get_global_value(6) < 3):
                self.get(qualifier_2).set_transparency(50)
            self.set_event_id(831)
            if (select(self.get(qualifier_2).values.get(2, 0) == 0) and
            self.get_global_value(6) < 3):
                self.get(qualifier_2).set_transparency(0)
        if self.groups['Layer']:
            self.set_event_id(835)
            if True:
                self.do_sort()
                self.groups['Layer'] = False
        if self.groups['Timer']:
            self.set_event_id(838)
            if self.every(0.01):
                self.get(Fusssoldat_193).AddToAlterable(10, 1)
            self.set_event_id(839)
            if (select(self.get(Fusssoldat_193).values.get(10, 0) >= 200) and
            select(self.get(DM_412).get_value() == 0) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 0)):
                self.groups['Timer'] = False
                self.get(Killed_203).set_value('Waiting for new round')
                self.get(Killed_203).set_visible(True)
            self.set_event_id(840)
            if select(self.get(Fusssoldat_193).values.get(10, 0) >= 200):
                self.get(Killed_203).set_visible(False)
                self.groups['Timer'] = False
        if self.groups['Chat']:
            self.set_event_id(843)
            if (Qt.Key_Return in self.scene.key_presses and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0)):
                RestoreControls()
                self.get(Fusssoldat_193).values[7] = 1
            self.set_event_id(844)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/closecon' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.groups['Con'] and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line('Command: All incoming connections are closed')
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.groups['Con'] = False
                self.get(Chat_204).set_focus(False)
            self.set_event_id(845)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/closecon' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            negate(self.groups['Con']) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line('Command: All Incoming connections already closed')
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(846)
            if (Qt.Key_Return in self.scene.key_presses and
            mid_string(self.get(Chat_204).get_value(), 0, 6) == '/kick ' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line('Command: Kick player '+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-6))
                self.get(Msg_427).set_value('117'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-6))
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(847)
            if (Qt.Key_Return in self.scene.key_presses and
            mid_string(self.get(Chat_204).get_value(), 0, 5) == '/ban ' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line('Command: Ban player '+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5))
                self.get(Msg_427).set_value('118'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5))
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(848)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/restart' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1 and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(DM_412).get_value() == 0) and
            select(self.get(GlobalValues_165).values.get(0, 0) == 1) and
            negate(self.groups['Map change'])):
                self.get(GlobalValues_165).values[1] = immediate_compare(to_number(self.get(Mapcycle_417).get_line(1)), '<', 1, 60, to_number(self.get(Mapcycle_417).get_line(1))*60)
            self.set_event_id(849)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/restart' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1 and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(DM_412).get_value() == 0) and
            negate(self.groups['Map change'])):
                self.groups['Chat'] = False
                self.add_hud_line('Command: Restart game')
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(RoundStart_361).set_value(2)
                self.get(ScorePolice_368).set_value(0)
                self.get(ScoreTerror_369).set_value(0)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.get(Money_366).set_value(0)
                self.get(Active6_214).set_visible(False)
                self.get(Fusssoldat_193).values[12] = 0
                self.get(FlashTime_381).set_value(0)
                self.get(InvincibleTime_388).set_value(7)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('218'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
                self.function_sendall()
                self.function_csmup()
                self.get(String31_437).set_value('0')
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(850)
            if (Qt.Key_Return in self.scene.key_presses and
            mid_string(self.get(Chat_204).get_value(), 0, 5) == '/map ' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1 and
            negate(os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5)+'.sdo'))):
                self.groups['Chat'] = False
                self.add_hud_line('Command: Map change failed - Map '+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5)+' not found')
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(851)
            if (Qt.Key_Return in self.scene.key_presses and
            mid_string(self.get(Chat_204).get_value(), 0, 5) == '/map ' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1 and
            os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5)+'.sdo')):
                self.get(qualifier_1).destroy()
                self.get(qualifier_2).destroy()
                self.get(qualifier_3).destroy()
                self.get(AmmoPack_208).destroy()
                self.get(SpawnArea_192).destroy()
                self.get(Nade_458).destroy()
                self.get(C4_374).destroy()
                self.get(Nade2_459).destroy()
                self.get(Gaswolke_215).destroy()
                self.get(GrenadeSpot_398).destroy()
                self.get(Exp_247).destroy()
                self.get(Molotov_450).destroy()
                self.get(Active17_451).destroy()
                self.get(P1_452).destroy()
                self.get(FlameDmg_456).destroy()
                self.get(BigflameDmg_457).destroy()
                self.get(SmokeExp_460).destroy()
            self.set_event_id(852)
            if (Qt.Key_Return in self.scene.key_presses and
            mid_string(self.get(Chat_204).get_value(), 0, 5) == '/map ' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1 and
            os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5)+'.sdo')):
                ClearScreen((0, 0, 0))
                self.groups['Chat'] = False
                self.add_hud_line('Command: Change map to '+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5))
                self.get(ChosedMap_125).set_value(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5)+'.sdo')
                self.get(ChosedMapWithoutPath_126).set_value(right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5))
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(SpawnArea_192).destroy()
                self.get(qualifier_1).destroy()
                self.get(qualifier_2).destroy()
                self.get(qualifier_3).destroy()
                self.get(AmmoPack_208).destroy()
                self.get(ChangeMap_217).set_visible(True)
                self.get(ChangeMap_217).set_value('Game starts in a few seconds')
                self.get(Respawn_201).set_value(20)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.groups['Map change'] = True
                self.get(FlashTime_381).set_value(0)
                self.get(RoundStart_361).set_value(0)
                self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+','+self.get(Version_26).text+','+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.groups['Load Map'] = True
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(853)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/resettime' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            select(self.get(GlobalValues_165).values.get(0, 0) == 1) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line('Command: Reset time')
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(GlobalValues_165).values[1] = immediate_compare(to_number(self.get(Mapcycle_417).get_line(1)), '<', 1, 60, to_number(self.get(Mapcycle_417).get_line(1))*60)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('224'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'Server resets time'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(854)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/resettime' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            select(self.get(GlobalValues_165).values.get(0, 0) == 0) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line('No map cycle')
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(855)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/timeleft' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 0):
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('120'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(856)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/timeleft' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line(immediate_compare(self.get(GlobalValues_165).values[0], '=', 0, 'No map cycle', str(self.get(GlobalValues_165).values[1]/60)+':'+immediate_compare((self.get(GlobalValues_165).values[1]%60), '<', 10, '0'+str(self.get(GlobalValues_165).values[1]%60), str(self.get(GlobalValues_165).values[1]%60))+' min left'))
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(857)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/nextmap' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 0):
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('121'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(858)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/nextmap' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.add_hud_line(immediate_compare(self.get(GlobalValues_165).values[0], '=', 0, 'No map cycle', immediate_compare(self.get(GlobalValues_165).values[2], '<', 'self.get(Mapcycle_417).ListGetLineCount', 'Next map is '+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2]+1), 'Next map is '+self.get(Mapcycle_417).get_line(2))))
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(859)
            if (Qt.Key_Return in self.scene.key_presses and
            left_string(self.get(Chat_204).get_value(), 5) == '/msg ' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            self.get_global_value(1) == 1):
                self.groups['Chat'] = False
                self.get(Msg_427).set_value('222'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5)+str(self.get(Csm_432).get_value()))
                self.get(ChangeMap_217).set_value(right_string(self.get(Chat_204).get_value(), len(self.get(Chat_204).get_value())-5))
                self.add_hud_line('Command: Noticeable message')
                self.get(MsgCounter_332).set_value(10)
                self.groups['Msg'] = True
                self.get(ChangeMap_217).set_visible(True)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(860)
            if (Qt.Key_Return in self.scene.key_presses and
            left_string(self.get(Chat_204).get_value(), 2) == '//' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Mode_344).get_value() == 1)):
                self.groups['Chat'] = False
                self.get(Msg_427).set_value('221'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+right_string(self.get(Chat_204).get_value(), (len(self.get(Chat_204).get_value())-2))+str(self.get(Csm_432).get_value()))
                self.add_hud_line(self.get(RealName_390).text+'(Team): '+right_string(self.get(Chat_204).get_value(), (len(self.get(Chat_204).get_value())-2)))
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(861)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() != '' and
            left_string(self.get(Chat_204).get_value(), 1) != '/' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0)):
                self.groups['Chat'] = False
                self.add_hud_line(self.get(RealName_390).text+': '+self.get(Chat_204).get_value())
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('206'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+self.get(Chat_204).get_value()+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(862)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join police' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) == 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 1) and
            self.get_global_value(1) == 0 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join police')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 0
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(863)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join terrorists' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) == 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 2) and
            self.get_global_value(1) == 0 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join terrorists')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 0
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(864)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join police' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) == 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 1) and
            self.get_global_value(1) == 0 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join police')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 0
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(865)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join terrorists' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) == 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 2) and
            self.get_global_value(1) == 0 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join terrorists')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 0
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(866)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join police' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) > 0) and
            select(self.get(Fusssoldat_193).values.get(5, 0) < 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 1) and
            self.get_global_value(1) == 0 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join police')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 0
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(Frags_209).subtract_value(1)
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(SvrKills2_32).subtract_value(1)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'1'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(867)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join terrorists' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) > 0) and
            select(self.get(Fusssoldat_193).values.get(5, 0) < 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 2) and
            self.get_global_value(1) == 0 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join terrorists')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 0
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(Frags_209).subtract_value(1)
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.groups['Chat'] = False
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(SvrKills2_32).subtract_value(1)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'1'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(868)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join police' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) == 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 1) and
            self.get_global_value(1) == 1 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join police')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(869)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join terrorists' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) == 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 2) and
            self.get_global_value(1) == 1 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join terrorists')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(870)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join police' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) <= 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 1) and
            self.get_global_value(1) == 1 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join police')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(871)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join terrorists' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) <= 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 2) and
            self.get_global_value(1) == 1 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join terrorists')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'0'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(872)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join police' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) > 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) < 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 1) and
            self.get_global_value(1) == 1 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join police')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.groups['Chat'] = False
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(Frags_209).subtract_value(1)
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(SvrKills2_32).subtract_value(1)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'1'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(873)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '/join terrorists' and
            negate(self.groups['Join Team']) and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) > 1) and
            select(self.get(Fusssoldat_193).values.get(5, 0) < 100) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 0) and
            select(self.get(Fusssoldat_193).values.get(8, 0) != 2) and
            self.get_global_value(1) == 1 and
            negate(self.groups['Map change'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.add_hud_line('Command: Join terrorists')
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Active6_214).set_visible(False)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Counter3_246).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.get(Fusssoldat_193).values[22] = 0
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(Frags_209).subtract_value(1)
                self.get(DurchlaufChat_245).set_value(0)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.groups['Chat'] = False
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(FlashTime_381).set_value(0)
                self.get(Killed_203).set_value(immediate_compare(self.get(DM_412).get_value(), '=', 0, 'Waiting for new round', ''))
                self.get(Killed_203).set_visible(True)
                self.groups['Change team respawn dm'] = True
                self.get(Respawntext_392).set_visible(False)
                self.get(SvrKills2_32).subtract_value(1)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Msg_427).set_value('217'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'1'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(874)
            if self.every(0.2):
                self.get(Chat_204).set_focus(True)
            self.set_event_id(875)
            if (Qt.Key_Return in self.scene.key_presses and
            self.get(Chat_204).get_value() == '' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0)):
                self.groups['Chat'] = False
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(876)
            if (Qt.Key_Return in self.scene.key_presses and
            left_string(self.get(Chat_204).get_value(), 1) == '/' and
            select(self.get(Fusssoldat_193).values.get(23, 0) == 0)):
                self.groups['Chat'] = False
                self.add_hud_line('Invalid command')
                self.get(ChattingPlayer_356).values[1] = 0
                self.get(ChattingPlayer_356).set_position(132, 659) # {'y': 659, 'x': 132}
                self.get(DurchlaufChat_245).set_value(0)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('205'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
            self.set_event_id(877)
            if select(self.get(Fusssoldat_193).values.get(23, 0) == 1):
                self.get(Fusssoldat_193).values[23] = 0
            self.set_event_id(878)
            if True:
                self.get(ChattingPlayer_356).set_position(self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + -15) # {'y': -15, 'x': 0, 'parent': 'self.get(Fusssoldat_193)'}
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Strafing_219).movement.stop()
        if self.groups['Map change']:
            self.set_event_id(881)
            if (select(self.get(GlobalValues_165).values.get(0, 0) == 1) and
            self.not_always()):
                self.get(GlobalValues_165).values[1] = immediate_compare(to_number(self.get(Mapcycle_417).get_line(1)), '<', 1, 60, to_number(self.get(Mapcycle_417).get_line(1))*60)
            self.set_event_id(882)
            if (True and
            self.not_always()):
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(Respawntext_392).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.get(Strafing_219).set_position(920, 95) # {'y': 95, 'x': 920}
                self.get(Strafing2_220).set_position(933, 178) # {'y': 178, 'x': 933}
                self.get(Killed_203).set_value('')
                self.get(Killed_203).set_visible(False)
                self.groups['Timer'] = False
                self.get(Fusssoldat_193).values[10] = 0
                self.groups['Join Team'] = False
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat2_194).values[25] = 0
                self.get(Fusssoldat_193).values[5] = 100
                self.get(Strafing2_220).values[25] = 0
            self.set_event_id(883)
            if (True and
            self.not_always()):
                self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
            self.set_event_id(884)
            if (True and
            self.not_always()):
                self.get(ScoreBoard_231).add_line(str(self.get(Frags_209).get_value())+','+self.get(RealName_390).text+','+str(self.get(VisibleId_424).get_value())+','+str(self.get(Ping_233).get_value())+','+str(self.get(Deaths_210).get_value())+',1')
                self.get(ScoreBar_234).set_visible(True)
                self.get(NameScore_235).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore_236).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore_237).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing_307).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore2_347).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore2_348).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore2_349).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing2_350).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore3_351).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore3_352).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore3_353).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing3_354).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(PlOnlineText_316).set_visible(True)
                self.get(Players_317).set_visible(True)
                self.get(Fusssoldat_193).flags[20] = True
                self.get(Fusssoldat_193).flags[21] = True
                for loop_index in xrange('self.get(Fusssoldat2_194).ObjectCount'):
                    if self.loop_entry(loop_index) == False: break
                for loop_index in xrange('self.get(ScoreBoard_231).ListGetLineCount'):
                    if self.loop_list(loop_index) == False: break
            self.set_event_id(885)
            if select(self.get(Fusssoldat_193).flags[20] == True):
                self.get(Fusssoldat_193).flags[20] = False
                self.get(Fusssoldat2_194).values[18] = 0
                self.get(Fusssoldat2_194).values[7] = 0
                self.get(Fusssoldat2_194).values[8] = 0
            self.set_event_id(886)
            if (select(self.get(Respawn_201).get_value() == 5) and
            self.not_always() and
            self.get(ChangeMap_217).text == 'Game starts in a few seconds' and
            select(self.get(Respawn_201).visible)):
                self.get(ChangeMap_217).set_visible(False)
                self.get(ChangeMap_217).set_value('')
            self.set_event_id(887)
            if (select(self.get(Respawn_201).get_value() == 5) and
            self.get_global_value(1) == 1 and
            select(self.get(Respawn_201).visible) and
            self.not_always()):
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
                self.groups['Map change'] = False
                self.get(Frags_209).set_value(0)
                self.get(Deaths_210).set_value(0)
                self.get(Mode_344).set_value(0)
                self.get(Fusssoldat_193).values[8] = self.get_global_value(4)
                self.get(DM_412).set_value(1)
            self.set_event_id(888)
            if (select(self.get(Respawn_201).get_value() == 5) and
            self.get_global_value(1) == 0 and
            select(self.get(Respawn_201).visible) and
            self.not_always()):
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
                self.groups['Map change'] = False
                self.get(Frags_209).set_value(0)
                self.get(Deaths_210).set_value(0)
                self.get(Mode_344).set_value(0)
                self.get(Fusssoldat_193).values[8] = self.get_global_value(4)
                self.get(DM_412).set_value(1)
            self.set_event_id(889)
            if True:
                self.values[3] = 0
            self.set_event_id(890)
            if select(self.get(Respawn_201).get_value() > 10):
                self.get(AmmoPack_208).destroy()
            self.set_event_id(891)
            if (self.every(1.0) and
            select(self.get(Respawn_201).get_value() > 1) and
            select(self.get(Respawn_201).ObjectInvisible())):
                self.get(Respawn_201).subtract_value(1)
            self.set_event_id(892)
            if (select(self.get(Respawn_201).get_value() == 1) and
            self.not_always() and
            self.get(ChangeMap_217).text == 'Game starts in a few seconds' and
            select(self.get(Respawn_201).ObjectInvisible()) and
            self.not_always()):
                self.get(ChangeMap_217).set_visible(False)
                self.get(ChangeMap_217).set_value('')
            self.set_event_id(893)
            if (select(self.get(Respawn_201).get_value() == 1) and
            select(self.get(Respawn_201).ObjectInvisible()) and
            select(self.get(Modestatus_413).get_value() == 1) and
            self.not_always()):
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
                self.groups['Map change'] = False
                self.get(Frags_209).set_value(0)
                self.get(Deaths_210).set_value(0)
                self.get(Mode_344).set_value(1)
                self.get(Respawn_201).set_value(9)
                self.groups['Join Team'] = True
                self.get(Police_342).set_visible(True)
                self.get(Terror_343).set_visible(True)
                self.get(Fusssoldat_193).values[8] = 0
                self.get(DM_412).set_value(0)
            self.set_event_id(894)
            if (select(self.get(Respawn_201).get_value() == 1) and
            select(self.get(Respawn_201).ObjectInvisible()) and
            select(self.get(Modestatus_413).get_value() == 2) and
            self.not_always()):
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
                self.groups['Map change'] = False
                self.get(Frags_209).set_value(0)
                self.get(Deaths_210).set_value(0)
                self.get(Mode_344).set_value(1)
                self.get(Respawn_201).set_value(9)
                self.groups['Join Team'] = True
                self.get(Police_342).set_visible(True)
                self.get(Terror_343).set_visible(True)
                self.get(Fusssoldat_193).values[8] = 0
                self.get(DM_412).set_value(0)
            self.set_event_id(895)
            if (select(self.get(Respawn_201).get_value() == 1) and
            select(self.get(Respawn_201).ObjectInvisible()) and
            select(self.get(Modestatus_413).get_value() == 3) and
            self.not_always()):
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
                self.groups['Map change'] = False
                self.get(Frags_209).set_value(0)
                self.get(Deaths_210).set_value(0)
                self.get(Mode_344).set_value(1)
                self.get(Respawn_201).set_value(9)
                self.groups['Join Team'] = True
                self.get(Police_342).set_visible(True)
                self.get(Terror_343).set_visible(True)
                self.get(Fusssoldat_193).values[8] = 0
                self.get(DM_412).set_value(1)
            self.set_event_id(896)
            if select(self.get(Strafing2_220).values.get(25, 0) == 0):
                self.get(Strafing2_220).set_position(933, 178) # {'y': 178, 'x': 933}
                self.get(Strafing2_220).movement.stop()
        if self.groups['Weapon Change']:
            self.set_event_id(899)
            if self.players[0].lives == 1:
                self.get(Obj1Weapon_308).force_animation('User defined 1')
                self.get(Obj2Weapon_309).restore_animation()
                self.get(AmmoCurrent_311).set_value(15)
                self.get(AmmoFull_312).set_value(0)
                self.get(Fusssoldat_193).values[20] = 0
                for item in self.get(Active5_213, True):
                    item.destroy()
                self.groups['W1'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(SecondWeapon_318).set_value(0)
                self.get(Ammo1_321).set_value(0)
                self.get(Ammo2_322).set_value(0)
                self.get(Reload2_323).set_value(0)
                self.get(Obj2WeaponList_315).set_direction(10)
                for item in self.get(Fusssoldat2_194, True):
                    item.values[19] = 0
            self.set_event_id(900)
            if self.players[0].lives == 2:
                self.get(Obj2WeaponList_315).set_direction(0)
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(AmmoCurrent_311).set_value(30)
                self.get(AmmoFull_312).set_value(1*self.get(DM_412).get_value())
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W2'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(901)
            if self.players[0].lives == 3:
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2WeaponList_315).set_direction(16)
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(AmmoCurrent_311).set_value(8)
                self.get(AmmoFull_312).set_value(1*self.get(DM_412).get_value())
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W3'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(902)
            if self.players[0].lives == 4:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(24)
                self.get(AmmoCurrent_311).set_value(7)
                self.get(AmmoFull_312).set_value(2*self.get(DM_412).get_value())
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 4'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(903)
            if self.players[0].lives == 5:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(8)
                self.get(AmmoCurrent_311).set_value(1)
                self.get(AmmoFull_312).set_value(2*self.get(DM_412).get_value())
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 5'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(904)
            if self.players[0].lives == 6:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(4)
                self.get(AmmoCurrent_311).set_value(30)
                self.get(AmmoFull_312).set_value(2*self.get(DM_412).get_value())
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 6'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(905)
            if self.players[0].lives == 7:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(28)
                self.get(AmmoCurrent_311).set_value(20)
                self.get(AmmoFull_312).set_value(0)
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 7'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(906)
            if self.players[0].lives == 8:
                self.get(Obj1Weapon_308).force_animation('User defined 1')
                self.get(Obj2Weapon_309).restore_animation()
                self.get(AmmoCurrent_311).set_value(13)
                self.get(AmmoFull_312).set_value(0)
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 8'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(SecondWeapon_318).set_value(0)
                self.get(Ammo1_321).set_value(0)
                self.get(Ammo2_322).set_value(0)
                self.get(Reload2_323).set_value(0)
                self.get(Obj2WeaponList_315).set_direction(10)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(907)
            if self.players[0].lives == 9:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(20)
                self.get(AmmoCurrent_311).set_value(30)
                self.get(AmmoFull_312).set_value(0)
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 9'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(908)
            if self.players[0].lives == 10:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(6)
                self.get(AmmoCurrent_311).set_value(25)
                self.get(AmmoFull_312).set_value(1*self.get(DM_412).get_value())
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 10'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(909)
            if self.players[0].lives == 11:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(2)
                self.get(AmmoCurrent_311).set_value(10)
                self.get(AmmoFull_312).set_value(1*self.get(DM_412).get_value())
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 11'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(910)
            if self.players[0].lives == 12:
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(30)
                self.get(AmmoCurrent_311).set_value(4)
                self.get(AmmoFull_312).set_value(2*self.get(DM_412).get_value())
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
                self.groups['W 12'] = True
                self.groups['Reload'] = False
                self.groups['Weapon Change'] = False
                self.get(ShotLatence_230).set_value(0)
                self.get(Fusssoldat2_194).values[19] = 0
        if self.groups['Weapon Change Normal']:
            self.set_event_id(913)
            if self.players[0].lives == 1:
                self.groups['W1'] = True
                self.get(Obj1Weapon_308).force_animation('User defined 1')
                self.get(Obj2Weapon_309).restore_animation()
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(914)
            if self.players[0].lives == 2:
                self.groups['W2'] = True
                self.get(Obj2WeaponList_315).set_direction(0)
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(915)
            if self.players[0].lives == 3:
                self.groups['W3'] = True
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2WeaponList_315).set_direction(16)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(916)
            if self.players[0].lives == 4:
                self.groups['W 4'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(24)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(917)
            if self.players[0].lives == 5:
                self.groups['W 5'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(8)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(918)
            if self.players[0].lives == 6:
                self.groups['W 6'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(4)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(919)
            if self.players[0].lives == 7:
                self.groups['W 7'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(28)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(920)
            if self.players[0].lives == 8:
                self.groups['W 8'] = True
                self.get(Obj1Weapon_308).force_animation('User defined 1')
                self.get(Obj2Weapon_309).restore_animation()
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(921)
            if self.players[0].lives == 9:
                self.groups['W 9'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(20)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(922)
            if self.players[0].lives == 10:
                self.groups['W 10'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(6)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(923)
            if self.players[0].lives == 11:
                self.groups['W 11'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(2)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
            self.set_event_id(924)
            if self.players[0].lives == 12:
                self.groups['W 12'] = True
                self.get(Obj1Weapon_308).restore_animation()
                self.get(Obj2Weapon_309).force_animation('User defined 1')
                self.get(Obj2WeaponList_315).set_direction(30)
                self.groups['Weapon Change Normal'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.groups['Reload'] = False
                self.get(Fusssoldat2_194).values[19] = 0
        if self.groups['Reload']:
            self.set_event_id(927)
            if select(self.get(Fusssoldat_193).values.get(20, 0) == 0):
                self.create_object(Active5_213, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + -20) # {'y': -20, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active5_213'}
                self.get(Active5_213).values[9] = 11000000
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('209'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'1'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(928)
            if (self.every(0.01) and
            select(self.get(Fusssoldat_193).values.get(20, 0) < 200)):
                self.get(Fusssoldat_193).AddToAlterable(20, 1)
                self.get(Active5_213).set_position(self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + -20) # {'y': -20, 'x': 0, 'parent': 'self.get(Fusssoldat_193)'}
            self.set_event_id(929)
            if select(self.get(Fusssoldat_193).values.get(20, 0) == 100):
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('209'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'2'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('clipin.wav')
            self.set_event_id(930)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 170) and
            self.players[0].lives == 1):
                self.get(AmmoCurrent_311).set_value(15)
            self.set_event_id(931)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 200) and
            self.players[0].lives == 2):
                self.get(AmmoCurrent_311).set_value(30)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(932)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 200) and
            self.players[0].lives == 3):
                self.get(AmmoCurrent_311).set_value(8)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(933)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 150) and
            self.players[0].lives == 4):
                self.get(AmmoCurrent_311).set_value(7)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(934)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 160) and
            self.players[0].lives == 5):
                self.get(AmmoCurrent_311).set_value(1)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(935)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 200) and
            self.players[0].lives == 6):
                self.get(AmmoCurrent_311).set_value(30)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(936)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 200) and
            self.players[0].lives == 7):
                self.get(AmmoCurrent_311).set_value(20)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(937)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 180) and
            self.players[0].lives == 8):
                self.get(AmmoCurrent_311).set_value(13)
            self.set_event_id(938)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 200) and
            self.players[0].lives == 9):
                self.get(AmmoCurrent_311).set_value(30)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(939)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 200) and
            self.players[0].lives == 10):
                self.get(AmmoCurrent_311).set_value(25)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(940)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 200) and
            self.players[0].lives == 11):
                self.get(AmmoCurrent_311).set_value(10)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(941)
            if (select(self.get(Fusssoldat_193).values.get(20, 0) == 160) and
            self.players[0].lives == 12):
                self.get(AmmoCurrent_311).set_value(4)
                self.get(AmmoFull_312).subtract_value(1)
            self.set_event_id(942)
            if select(self.get(AmmoCurrent_311).get_value() >= 1):
                self.groups['Reload'] = False
                self.get(Fusssoldat_193).values[20] = 0
                self.get(Active5_213).destroy()
        if self.groups['Grenades']:
            self.set_event_id(945)
            if select(self.get(Fusssoldat_193).values.get(12, 0) == 1):
                self.get(Active6_214).set_direction(0)
                self.get(Active6_214).BringToFront()
                self.get(Active6_214).set_visible(True)
                self.groups['Grenades'] = False
            self.set_event_id(946)
            if select(self.get(Fusssoldat_193).values.get(12, 0) == 2):
                self.get(Active6_214).set_direction(24)
                self.get(Active6_214).BringToFront()
                self.get(Active6_214).set_visible(True)
                self.groups['Grenades'] = False
            self.set_event_id(947)
            if select(self.get(Fusssoldat_193).values.get(12, 0) == 3):
                self.get(Active6_214).set_direction(8)
                self.get(Active6_214).BringToFront()
                self.get(Active6_214).set_visible(True)
                self.groups['Grenades'] = False
            self.set_event_id(948)
            if select(self.get(Fusssoldat_193).values.get(12, 0) == 4):
                self.get(Active6_214).set_direction(16)
                self.get(Active6_214).BringToFront()
                self.get(Active6_214).set_visible(True)
                self.groups['Grenades'] = False
            self.set_event_id(949)
            if select(self.get(Fusssoldat_193).values.get(12, 0) == 5):
                self.get(Active6_214).set_direction(4)
                self.get(Active6_214).BringToFront()
                self.get(Active6_214).set_visible(True)
                self.groups['Grenades'] = False
            self.set_event_id(950)
            if select(self.get(Fusssoldat_193).values.get(12, 0) == 6):
                self.get(Active6_214).set_direction(12)
                self.get(Active6_214).BringToFront()
                self.get(Active6_214).set_visible(True)
                self.groups['Grenades'] = False
        if self.groups['Server']:
            self.set_event_id(953)
            if self.every(15.0):
                self.values[3] = 0
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('220'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(954)
            if self.every(6.0):
                self.get(Fusssoldat2_194).AddToAlterable(13, 1)
            self.set_event_id(955)
            if select(self.get(Fusssoldat2_194).values.get(13, 0) >= 10):
                self.get(Fusssoldat_193).flags[24] = False
                self.get(Fusssoldat2_194).values[13] = 0
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value(str(self.get(Fusssoldat2_194).values[0]))
                self.function_pleft()
                self.function_pleftsend()
            self.set_event_id(956)
            if (select(self.get(Fusssoldat2_194).values.get(19, 0) > 0) and
            select(self.get(Strafing_219).values.get(5, 0) > 2)):
                self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat2_194).values[6] = immediate_compare(self.get(Fusssoldat2_194).values[19], '<', 300, self.get(Fusssoldat2_194).values[19]/5, ((self.get(Fusssoldat2_194).values[19]-300)/5)*-1)
                self.get(Msg_427).set_value('112'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat2_194).values[19], 0)+self.get(Fusssoldat2_194).values[12]*1000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat2_194).values[19] -= immediate_compare(self.get(Fusssoldat2_194).values[19], '<', 300, 0, 300)
                self.get(Fusssoldat2_194).values[24] -= immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat2_194).values[19], 0)
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Active7_195).destroy()
                self.get(Fusssoldat2_194).values[5] = 1
                self.get(Fusssoldat2_194).values[19] = 0
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(957)
            if select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0):
                self.groups['Server other Player'] = True
            self.set_event_id(958)
            if select(self.get(Fusssoldat_193).values.get(5, 0) <= 0):
                self.groups['Server Player'] = True
            self.set_event_id(959)
            if (Qt.Key_Space in self.scene.key_presses and
            select(self.get(Respawntext_392).visible) and
            self.get_global_value(2) == 0 and
            self.get_global_value(1) == 1 and
            select(self.get(Mode_344).get_value() == 0) and
            select(self.get(DM_412).get_value() == 1) and
            negate(self.groups['Chat'])):
                self.get(PingCounter_232).set_value(0)
                self.get(Respawntext_392).set_visible(False)
                for loop_index in xrange(100):
                    if self.loop_spawn(loop_index) == False: break
            self.set_event_id(960)
            if (Qt.Key_Space in self.scene.key_presses and
            select(self.get(Respawntext_392).visible) and
            self.get_global_value(2) == 0 and
            self.get_global_value(1) == 1 and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(DM_412).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
            negate(self.groups['Chat'])):
                self.get(PingCounter_232).set_value(0)
                self.get(Respawntext_392).set_visible(False)
                for loop_index in xrange(100):
                    if self.loop_spawn_p(loop_index) == False: break
            self.set_event_id(961)
            if (Qt.Key_Space in self.scene.key_presses and
            select(self.get(Respawntext_392).visible) and
            self.get_global_value(2) == 0 and
            self.get_global_value(1) == 1 and
            select(self.get(Mode_344).get_value() == 1) and
            select(self.get(DM_412).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
            negate(self.groups['Chat'])):
                self.get(PingCounter_232).set_value(0)
                self.get(Respawntext_392).set_visible(False)
                for loop_index in xrange(100):
                    if self.loop_spawn_t(loop_index) == False: break
            self.set_event_id(968)
            if (select(self.get(Fusssoldat_193).IsOverlapping(Gaswolke_215)) and
            self.every(0.1) and
            select(self.get(Fusssoldat_193).values.get(0, 0) == self.get(Gaswolke_215).values[1]) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat_193).values[25] = self.get(VisibleId_424).get_value()
                self.get(Fusssoldat_193).AddToAlterable(15, 2+randrange(3))
            self.set_event_id(969)
            if select(self.get(Fusssoldat_193).values.get(15, 0) >= 25):
                self.create_object(Active2_254, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat_193).values[15] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat_193).values[15], 0)
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[15]+self.get(VisibleId_424).get_value()*1000+100000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat_193).values[5] -= self.get(Fusssoldat_193).values[15]
                self.get(Fusssoldat_193).values[6] = 10
                self.get(Fusssoldat_193).values[15] = 0
                self.get(Fusssoldat_193).values[16] = 1
                self.get(Fusssoldat_193).values[25] = self.get(VisibleId_424).get_value()
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundAutoPlay('hit.wav')
            self.set_event_id(970)
            if (select(self.get(Fusssoldat2_194).IsOverlapping(Gaswolke_215)) and
            self.every(0.1) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1) and
            select(self.get(Gaswolke_215).values.get(1, 0) == self.get(Fusssoldat_193).values[0]) and
            select(self.get(InvincibleTime_388).get_value() == 0)):
                self.get(Fusssoldat2_194).AddToAlterable(15, 2+randrange(3))
                self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
            self.set_event_id(971)
            if (select(self.get(Fusssoldat2_194).values.get(15, 0) >= 25) and
            select(self.get(Fusssoldat2_194).values.get(25, 0) == 1)):
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.get(Active2_254).BringToBack()
                self.get(Fusssoldat2_194).values[15] = immediate_compare(self.get(InvincibleTime_388).get_value(), '=', 0, self.get(Fusssoldat2_194).values[15], 0)
                self.get(Msg_427).set_value('113'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[15]+self.get(Fusssoldat2_194).values[12]*1000+100000))+str(self.get(Csm_432).get_value()))
                self.get(Fusssoldat2_194).values[24] -= self.get(Fusssoldat2_194).values[15]
                self.get(Fusssoldat2_194).values[6] = 10
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(Fusssoldat2_194).values[5] = 1
                self.get(Fusssoldat2_194).values[23] = self.get(VisibleId_424).get_value()
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('hit.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(989)
            if (self.every(1.0) and
            select(self.get(RoundStart_361).get_value() > 1)):
                self.get(RoundStart_361).subtract_value(1)
            self.set_event_id(990)
            if (self.every(1.0) and
            select(self.get(RoundStart_361).get_value() == 1)):
                self.get(Strafing_219).flags[11] = True
            self.set_event_id(991)
            if (select(self.get(Strafing_219).flags[11] == True) and
            select(self.get(Gaswolke_215).values.get(0, 0) >= 0)):
                self.get(Gaswolke_215).destroy()
            self.set_event_id(992)
            if (select(self.get(Strafing_219).flags[11] == True) and
            select(self.get(Active17_451).values.get(0, 0) >= 0)):
                self.get(Active17_451).destroy()
            self.set_event_id(993)
            if (select(self.get(Strafing_219).flags[11] == True) and
            select(self.get(P1_452).values.get(0, 0) >= 0)):
                self.get(P1_452).destroy()
            self.set_event_id(994)
            if (select(self.get(Strafing_219).flags[11] == True) and
            select(self.get(FlameDmg_456).values.get(0, 0) >= 0)):
                self.get(FlameDmg_456).destroy()
            self.set_event_id(995)
            if (select(self.get(Strafing_219).flags[11] == True) and
            select(self.get(BigflameDmg_457).values.get(0, 0) >= 0)):
                self.get(BigflameDmg_457).destroy()
            self.set_event_id(996)
            if (select(self.get(Strafing_219).flags[11] == True) and
            select(self.get(SmokeExp_460).values.get(9, 0) >= 0)):
                self.get(SmokeExp_460).destroy()
            self.set_event_id(997)
            if select(self.get(Strafing_219).flags[11] == True):
                self.get(Strafing_219).flags[11] = False
                self.get(PoliceWin_362).set_position(-49, 688) # {'y': 688, 'x': -49}
                self.get(TerrorWin_363).set_position(-49, 688) # {'y': 688, 'x': -49}
                self.get(Counter3_246).set_value(0)
                self.get(Gaswolke_215).destroy()
                self.get(Nade_458).destroy()
                self.get(Exp_247).destroy()
                self.get(C4_374).destroy()
                self.get(WallDestroyed_376).destroy()
                self.get(qualifier_6).restore_animation()
                self.get(BoxDestroyed_377).destroy()
                self.get(Box_287).restore_animation()
                self.get(Nade2_459).destroy()
                self.get(FlashTime_381).set_value(0)
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(GrenadeSpot_398).destroy()
                self.get(Pipeline_403).restore_animation()
                self.get(PipelineDestroyed_411).destroy()
                self.get(PoliceCar_275).restore_animation()
                self.get(PoliceCar2_276).restore_animation()
                self.get(Reclist_426).reset()
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('214'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value())))
                self.function_sendall()
                self.function_csmup()
                self.get(Snipercounter_438).set_value(0)
                self.get(Molotov_450).destroy()
                self.get(Active17_451).destroy()
                self.get(P1_452).destroy()
                self.get(FlameDmg_456).destroy()
                self.get(BigflameDmg_457).destroy()
                self.get(SmokeExp_460).destroy()
            self.set_event_id(998)
            if (select(self.get(InvincibleTime_388).get_value() == 0) and
            self.not_always()):
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
            self.set_event_id(999)
            if (self.every(1.0) and
            select(self.get(RoundStart_361).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
            select(self.get(PoliceSpawn_345).PickRandom())):
                self.get(Fusssoldat_193).values[5] = 100
                self.get(Strafing_219).set_position(self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)'}
                self.get(Fusssoldat_193).set_visible(True)
                self.get(Strafing_219).movement.stop()
                self.get(Fusssoldat_193).values[14] = 1
                self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
                self.get(Oben_239).set_visible(True)
                self.get(Unten_240).set_visible(True)
                self.get(Rechts_241).set_visible(True)
                self.get(Links_242).set_visible(True)
                self.get(Strafing_219).values[18] = -1
                self.create_object(MagicExplode3_212, self.get(PoliceSpawn_345).x + 0, self.get(PoliceSpawn_345).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(PoliceSpawn_345)', 'create_object': 'MagicExplode3_212'}
                self.get(SkillCounter_211).set_value(0)
                self.get(Killed_203).set_value('')
                self.get(Killed_203).set_visible(False)
                self.function_write_shop()
                self.groups['reset standard'] = True
                self.groups['Shop'] = True
                self.get(ShopList_370).set_visible(True)
                self.get(ShopListPrice_371).set_visible(True)
                self.get(Money_366).add_value(1500)
                self.get(Shop1Blitter_372).set_visible(True)
                self.get(Shop2Blitter_373).set_visible(True)
                self.get(WallDestroyed_376).destroy()
                self.get(qualifier_6).restore_animation()
                self.get(BoxDestroyed_377).destroy()
                self.get(Box_287).restore_animation()
                self.get(Shop1Blitter2_385).set_visible(True)
                self.get(Shop1Blitter3_386).set_visible(True)
                self.get(Fusssoldat_193).values[15] = 0
                self.get(Pipeline_403).restore_animation()
                self.get(PipelineDestroyed_411).destroy()
                self.get(PoliceCar_275).restore_animation()
                self.get(PoliceCar2_276).restore_animation()
                self.get(Active9_222).values[7] = 0
                self.get(Oben_239).restore_animation()
                self.get(Unten_240).restore_animation()
                self.get(Rechts_241).restore_animation()
                self.get(Links_242).restore_animation()
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+1500))
            self.set_event_id(1000)
            if (self.every(1.0) and
            select(self.get(RoundStart_361).get_value() == 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
            select(self.get(TerrorSpawn_346).PickRandom())):
                self.get(Fusssoldat_193).values[5] = 100
                self.get(Strafing_219).set_position(self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)'}
                self.get(Fusssoldat_193).set_visible(True)
                self.get(Strafing_219).movement.stop()
                self.get(Fusssoldat_193).values[14] = 1
                self.get(Msg_427).set_value('200'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Strafing_219).x+self.get(Strafing_219).y*1000+self.get(Ping_233).get_value()*1000000))+str(self.get(Csm_432).get_value()))
                self.get(Oben_239).set_visible(True)
                self.get(Unten_240).set_visible(True)
                self.get(Rechts_241).set_visible(True)
                self.get(Links_242).set_visible(True)
                self.get(Strafing_219).values[18] = -1
                self.create_object(MagicExplode3_212, self.get(TerrorSpawn_346).x + 0, self.get(TerrorSpawn_346).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(TerrorSpawn_346)', 'create_object': 'MagicExplode3_212'}
                self.get(SkillCounter_211).set_value(0)
                self.get(Killed_203).set_value('')
                self.get(Killed_203).set_visible(False)
                self.function_write_shop()
                self.groups['reset standard'] = True
                self.groups['Shop'] = True
                self.get(ShopList_370).set_visible(True)
                self.get(ShopListPrice_371).set_visible(True)
                self.get(Money_366).add_value(1500)
                self.get(Shop1Blitter_372).set_visible(True)
                self.get(Shop2Blitter_373).set_visible(True)
                self.get(WallDestroyed_376).destroy()
                self.get(qualifier_6).restore_animation()
                self.get(BoxDestroyed_377).destroy()
                self.get(Box_287).restore_animation()
                self.get(Shop1Blitter2_385).set_visible(True)
                self.get(Shop1Blitter3_386).set_visible(True)
                self.get(Fusssoldat_193).values[15] = 0
                self.get(Pipeline_403).restore_animation()
                self.get(PipelineDestroyed_411).destroy()
                self.get(PoliceCar_275).restore_animation()
                self.get(PoliceCar2_276).restore_animation()
                self.get(Active9_222).values[7] = 0
                self.get(Oben_239).restore_animation()
                self.get(Unten_240).restore_animation()
                self.get(Rechts_241).restore_animation()
                self.get(Links_242).restore_animation()
                self.get(NotID_430).set_value(0)
                self.function_sendall()
                self.function_csmup()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+1500))
            self.set_event_id(1001)
            if (self.every(1.0) and
            select(self.get(RoundStart_361).get_value() == 1)):
                self.get(RoundStart_361).set_value(0)
                self.get(WallDestroyed_376).destroy()
                self.get(qualifier_6).restore_animation()
                self.get(BoxDestroyed_377).destroy()
                self.get(Box_287).restore_animation()
                self.get(Pipeline_403).restore_animation()
                self.get(PipelineDestroyed_411).destroy()
                self.get(PoliceCar_275).restore_animation()
                self.get(PoliceCar2_276).restore_animation()
        if self.groups['Mapcycle active']:
            self.set_event_id(1004)
            if (select(self.get(GlobalValues_165).values.get(1, 0) == 15) and
            self.not_always()):
                self.get(Fusssoldat_193).values[22] = 0
                self.add_hud_line(immediate_compare(self.get(GlobalValues_165).values[2], '<', 'self.get(Mapcycle_417).ListGetLineCount', 'Few seconds left, next map is '+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2]+1), 'Few seconds left, next map is '+self.get(Mapcycle_417).get_line(2)))
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('224'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+immediate_compare(self.get(GlobalValues_165).values[2], '<', 'self.get(Mapcycle_417).ListGetLineCount', 'Few seconds left, next map is '+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2]+1), 'Few seconds left, next map is '+self.get(Mapcycle_417).get_line(2))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(1005)
            if self.every(1.0):
                self.get(GlobalValues_165).values[1] -= 1
            self.set_event_id(1006)
            if (select(self.get(GlobalValues_165).values.get(1, 0) <= 0) and
            negate(self.groups['Mapcycle'])):
                self.groups['Mapcycle'] = True
                self.get(GlobalValues_165).AddToAlterable(2, 1)
        if self.groups['Mapcycle']:
            self.set_event_id(1009)
            if 'self.get(Mapcycle_417).ListGetLineCount' < self.get(GlobalValues_165).values[2]:
                self.get(GlobalValues_165).values[2] = 2
            self.set_event_id(1010)
            if negate(os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2])+'.sdo')):
                self.add_hud_line('Command: Map change failed - Map '+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2])+' not found')
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(GlobalValues_165).AddToAlterable(2, 1)
            self.set_event_id(1011)
            if os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2])+'.sdo'):
                self.get(qualifier_1).destroy()
                self.get(qualifier_2).destroy()
                self.get(qualifier_3).destroy()
                self.get(AmmoPack_208).destroy()
                self.get(SpawnArea_192).destroy()
            self.set_event_id(1012)
            if os.path.isfile(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2])+'.sdo'):
                ClearScreen((0, 0, 0))
                self.add_hud_line('Command: Change map to '+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2]))
                self.get(ChosedMap_125).set_value(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'Maps\\'+self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2])+'.sdo')
                self.get(ChosedMapWithoutPath_126).set_value(self.get(Mapcycle_417).get_line(self.get(GlobalValues_165).values[2]))
                self.get(Fusssoldat_193).values[22] = 0
                self.get(DurchlaufChat_245).set_value(0)
                self.get(SpawnArea_192).destroy()
                self.get(qualifier_1).destroy()
                self.get(qualifier_2).destroy()
                self.get(qualifier_3).destroy()
                self.get(AmmoPack_208).destroy()
                self.get(ChangeMap_217).set_visible(True)
                self.get(ChangeMap_217).set_value('Game starts in a few seconds')
                self.get(Respawn_201).set_value(20)
                self.groups['Map change'] = True
                self.get(FlashTime_381).set_value(0)
                self.groups['Load Map'] = True
                self.groups['Mapcycle'] = False
                self.get(GlobalValues_165).values[1] = immediate_compare(to_number(self.get(Mapcycle_417).get_line(1)), '<', 1, 60, to_number(self.get(Mapcycle_417).get_line(1))*60)
                self.get(Svrmotd_428).set_value(self.get(ChosedMapWithoutPath_126).text+','+self.get(Mapid_397).text+','+self.get(MessageOfDay_58).text+','+self.get(WeaponAllowed_59).text+','+self.get(Version_26).text+','+str(self.get(Players_317).get_value())+','+str(self.get(MaxPlayer_102).get_value())+','+self.get(SvrPw_155).text)
        if self.groups['Server other Player']:
            self.set_event_id(1015)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) == 1) and
            select(self.get(DM_412).get_value() == 1)):
                self.get(ScoreTerror_369).add_value(1)
            self.set_event_id(1016)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) == 2) and
            select(self.get(DM_412).get_value() == 1)):
                self.get(ScorePolice_368).add_value(1)
            self.set_event_id(1017)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) == 0)):
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.create_object(Obj2Die_199, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Obj2Die_199'}
                self.get(Obj2Die_199).values[9] = self.get(Obj2Die_199).y
                self.get(Fusssoldat2_194).AddToAlterable(8, 1)
                self.get(Obj2Die_199).values[6] = 8
            self.set_event_id(1018)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) == 1)):
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.create_object(Obj6Die_341, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Obj6Die_341'}
                self.get(Obj6Die_341).values[9] = self.get(Obj6Die_341).y
                self.get(Fusssoldat2_194).AddToAlterable(8, 1)
                self.get(Obj6Die_341).values[6] = 8
            self.set_event_id(1019)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) == 2)):
                self.create_object(Active2_254, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Active2_254'}
                self.create_object(Obj5Die_340, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'Obj5Die_340'}
                self.get(Obj5Die_340).values[9] = self.get(Obj5Die_340).y
                self.get(Fusssoldat2_194).AddToAlterable(8, 1)
                self.get(Obj5Die_340).values[6] = 8
            self.set_event_id(1020)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 2)):
                self.get(Fusssoldat2_194).AddToAlterable(8, 1)
            self.set_event_id(1021)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(23, 0) == self.get(VisibleId_424).get_value()) and
            select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) != self.get(Fusssoldat_193).values[8]+(10*(1-self.get(Mode_344).get_value())))):
                self.get(Active2_254).BringToBack()
                self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
                self.get(Strafing2_220).values[4] = 0
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You killed '+self.get(NameTag2_429).get_text())
                self.groups['Timer'] = True
                self.get(Frags_209).add_value(1)
                self.get(SkillCounter_211).add_value(1)
                self.get(Fusssoldat2_194).values[24] = 100
                self.get(Fusssoldat2_194).values[25] = 0
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(Strafing2_220).values[25] = 0
                self.get(Money_366).add_value(500)
                self.get(Strafing2_220).values[23] = 0
                self.get(Strafing2_220).values[24] = 0
                self.get(SvrKills2_32).add_value(1)
                self.get(SvrPoints2_34).add_value(self.get(Fusssoldat2_194).get_flag(1))
                self.get(Fusssoldat2_194).flags[1] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(VisibleId_424).get_value()+self.get(Fusssoldat2_194).values[12]*100+10000)))
                self.function_sendall()
                self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+500))
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('die.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1022)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(23, 0) != self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 1)):
                self.get(Active2_254).BringToBack()
                self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
                self.get(Strafing2_220).values[4] = 0
                self.get(Fusssoldat2_194).values[24] = 100
                self.get(Fusssoldat2_194).values[25] = 0
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(Strafing2_220).values[25] = 0
                self.get(Strafing2_220).values[23] = 0
                self.get(Strafing2_220).values[24] = 0
                self.get(Fusssoldat2_194).flags[1] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[23]+self.get(Fusssoldat2_194).values[12]*100+10000)))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('die.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1023)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(23, 0) == self.get(VisibleId_424).get_value()) and
            select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 2) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) != self.get(Fusssoldat_193).values[8]+(10*(1-self.get(Mode_344).get_value())))):
                self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
                self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
                self.get(Strafing2_220).values[4] = 0
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You killed '+self.get(NameTag2_429).get_text())
                self.groups['Timer'] = True
                self.get(Frags_209).add_value(1)
                self.get(SkillCounter_211).add_value(1)
                self.get(Fusssoldat2_194).values[24] = 100
                self.get(Fusssoldat2_194).values[25] = 0
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Strafing2_220).values[25] = 0
                self.get(Money_366).add_value(500)
                self.get(Strafing2_220).values[23] = 0
                self.get(Strafing2_220).values[24] = 0
                self.get(SvrKills2_32).add_value(1)
                self.get(SvrPoints2_34).add_value(self.get(Fusssoldat2_194).get_flag(1))
                self.get(Fusssoldat2_194).flags[1] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(VisibleId_424).get_value()+self.get(Fusssoldat2_194).values[12]*100+20000)))
                self.function_sendall()
                self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)+500))
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('burn.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1024)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(23, 0) != self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 2)):
                self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
                self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
                self.get(Strafing2_220).values[4] = 0
                self.get(Fusssoldat2_194).values[24] = 100
                self.get(Fusssoldat2_194).values[25] = 0
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Strafing2_220).values[25] = 0
                self.get(Strafing2_220).values[23] = 0
                self.get(Strafing2_220).values[24] = 0
                self.get(Fusssoldat2_194).flags[1] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat2_194).values[23]+self.get(Fusssoldat2_194).values[12]*100+20000)))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('burn.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1025)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(23, 0) == self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) == self.get(Fusssoldat_193).values[8]) and
            select(self.get(Mode_344).get_value() == 1)):
                self.get(Active2_254).BringToBack()
                self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
                self.get(Strafing2_220).values[4] = 0
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You killed a teammate')
                self.groups['Timer'] = True
                self.get(Frags_209).subtract_value(2)
                self.get(Fusssoldat2_194).values[24] = 100
                self.get(Fusssoldat2_194).values[25] = 0
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(Strafing2_220).values[25] = 0
                self.get(Money_366).set_value(0)
                self.get(Strafing2_220).values[23] = 0
                self.get(Strafing2_220).values[24] = 0
                self.get(SvrKills2_32).subtract_value(2)
                self.get(Fusssoldat2_194).flags[1] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(VisibleId_424).get_value()+self.get(Fusssoldat2_194).values[12]*100+10000)))
                self.function_sendall()
                self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(String31_437).set_value('0')
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('die.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1026)
            if (select(self.get(Fusssoldat2_194).values.get(24, 0) <= 0) and
            select(self.get(Strafing2_220).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(23, 0) == self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat2_194).values.get(5, 0) == 2) and
            select(self.get(Fusssoldat2_194).values.get(18, 0) == self.get(Fusssoldat_193).values[8]) and
            select(self.get(Mode_344).get_value() == 1)):
                self.create_object(FlameDie_333, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'FlameDie_333'}
                self.get(Strafing2_220).set_position(61, -87) # {'y': -87, 'x': 61}
                self.get(Strafing2_220).values[4] = 0
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You killed a teammate')
                self.groups['Timer'] = True
                self.get(Frags_209).subtract_value(2)
                self.get(Fusssoldat2_194).values[24] = 100
                self.get(Fusssoldat2_194).values[25] = 0
                self.get(Fusssoldat2_194).values[15] = 0
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.get(Strafing2_220).values[25] = 0
                self.get(Money_366).set_value(0)
                self.get(Strafing2_220).values[23] = 0
                self.get(Strafing2_220).values[24] = 0
                self.get(SvrKills2_32).subtract_value(2)
                self.get(Fusssoldat2_194).flags[1] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(VisibleId_424).get_value()+self.get(Fusssoldat2_194).values[12]*100+20000)))
                self.function_sendall()
                self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(String31_437).set_value('0')
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('die.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1027)
            if self.every(2.0):
                self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
                for loop_index in xrange('self.get(Fusssoldat2_194).ObjectCount'):
                    self.loop_indexes['Check health'] = loop_index
                    if self.loop_check_health() == False: break
        if self.groups['Server Player']:
            self.set_event_id(1032)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
            select(self.get(DM_412).get_value() == 1)):
                self.get(ScoreTerror_369).add_value(1)
            self.set_event_id(1033)
            if (select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
            select(self.get(DM_412).get_value() == 1)):
                self.get(ScorePolice_368).add_value(1)
            self.set_event_id(1034)
            if (select(self.get(Fusssoldat_193).values.get(16, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 0)):
                self.create_object(Obj1Die_255, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Obj1Die_255'}
                self.get(Obj1Die_255).values[9] = self.get(Obj1Die_255).y
                self.get(Obj1Die_255).values[6] = 8
            self.set_event_id(1035)
            if (select(self.get(Fusssoldat_193).values.get(16, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 1)):
                self.create_object(Obj3Die_338, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Obj3Die_338'}
                self.get(Obj3Die_338).values[9] = self.get(Obj3Die_338).y
                self.get(Obj3Die_338).values[6] = 8
            self.set_event_id(1036)
            if (select(self.get(Fusssoldat_193).values.get(16, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 2)):
                self.create_object(Obj4Die_339, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Obj4Die_339'}
                self.get(Obj4Die_339).values[9] = self.get(Obj4Die_339).y
                self.get(Obj4Die_339).values[6] = 8
            self.set_event_id(1037)
            if (select(self.get(Fusssoldat_193).values.get(16, 0) >= 1) and
            select(self.get(DM_412).get_value() == 1)):
                self.get(Respawn_201).set_visible(True)
                self.get(String2_200).set_visible(True)
            self.set_event_id(1038)
            if (select(self.get(Fusssoldat_193).values.get(25, 0) != self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat_193).values.get(16, 0) == 1) and
            select(self.get(Fusssoldat2_194).values.get(12, 0) == self.get(Fusssoldat_193).values[25]) and
            select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You were killed by '+self.get(NameTag2_429).get_text())
                self.groups['Timer'] = True
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[14] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(Fusssoldat_193).BringToBack()
                self.get(ActiveObject1_218).BringToBack()
                self.get(Active6_214).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(Counter3_246).set_value(0)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.groups['Server Player'] = False
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[25]+self.get(VisibleId_424).get_value()*100+10000)))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                SoundAutoPlay('die.wav')
            self.set_event_id(1039)
            if (select(self.get(Fusssoldat_193).values.get(25, 0) == self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat_193).values.get(16, 0) == 1)):
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You have committed suicide')
                self.groups['Timer'] = True
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[14] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(Fusssoldat_193).BringToBack()
                self.get(ActiveObject1_218).BringToBack()
                self.get(Active6_214).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(Frags_209).subtract_value(1)
                self.get(Counter3_246).set_value(0)
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.groups['Server Player'] = False
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(SvrKills2_32).subtract_value(1)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[25]+self.get(VisibleId_424).get_value()*100+10000)))
                self.function_sendall()
                self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                SoundAutoPlay('die.wav')
            self.set_event_id(1040)
            if (select(self.get(Fusssoldat_193).values.get(25, 0) != self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat_193).values.get(16, 0) == 2) and
            select(self.get(Fusssoldat2_194).values.get(12, 0) == self.get(Fusssoldat_193).values[25]) and
            select(self.get(NameTag2_429).values.get(0, 0) == self.get(Fusssoldat2_194).values[0])):
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You were killed by '+self.get(NameTag2_429).get_text())
                self.groups['Timer'] = True
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[14] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(Fusssoldat_193).BringToBack()
                self.get(ActiveObject1_218).BringToBack()
                self.get(Active6_214).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(Counter3_246).set_value(0)
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.groups['Server Player'] = False
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[25]+self.get(VisibleId_424).get_value()*100+20000)))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                SoundAutoPlay('burn.wav')
            self.set_event_id(1041)
            if (select(self.get(Fusssoldat_193).values.get(25, 0) == self.get(VisibleId_424).get_value()) and
            select(self.get(Fusssoldat_193).values.get(16, 0) == 2)):
                self.get(Fusssoldat_193).values[10] = 0
                self.get(Killed_203).set_visible(True)
                self.get(Killed_203).set_value('You have committed suicide')
                self.groups['Timer'] = True
                self.create_object(FlameDie_333, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'FlameDie_333'}
                self.players[0].set_ignore(True)
                self.players[0].lives = 1+7*self.get_global_value(9)
                self.get(Fusssoldat_193).values[12] = 0
                self.get(Fusssoldat_193).values[14] = 0
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).values[5] = 1
                self.get(Strafing_219).set_position(117, -78) # {'y': -78, 'x': 117}
                self.get(Strafing_219).movement.stop()
                self.get(Fusssoldat_193).BringToBack()
                self.get(ActiveObject1_218).BringToBack()
                self.get(Active6_214).set_visible(False)
                self.get(SkillCounter_211).set_value(0)
                self.get(Deaths_210).add_value(1)
                self.get(Oben_239).set_visible(False)
                self.get(Unten_240).set_visible(False)
                self.get(Rechts_241).set_visible(False)
                self.get(Links_242).set_visible(False)
                self.get(Frags_209).subtract_value(1)
                self.get(Counter3_246).set_value(0)
                self.get(FlameDie_333).values[9] = self.get(FlameDie_333).x+self.get(FlameDie_333).y*1000
                self.groups['Weapon Change'] = True
                self.groups['Shop'] = False
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.groups['Server Player'] = False
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
                self.get(SvrKills2_32).subtract_value(1)
                self.get(SvrDeaths2_33).add_value(1)
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('210'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Fusssoldat_193).values[25]+self.get(VisibleId_424).get_value()*100+20000)))
                self.function_sendall()
                self.get(Msg_427).set_value('211'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(Frags_209).get_value()))+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                SoundAutoPlay('burn.wav')
        if False:#self.groups['Custom Movement']:
            self.set_event_id(1045)
            if (negate(PlayerKeyDown(4)) and
            negate(PlayerKeyDown(8)) and
            negate(PlayerKeyDown(1)) and
            negate(PlayerKeyDown(2)) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            self.not_always()):
                self.get(Strafing_219).movement.stop()
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1046)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            select(self.get(Fusssoldat_193).values.get(21, 0) < -2)):
                self.get(Fusssoldat_193).values[21] = 1
            self.set_event_id(1047)
            if (PlayerKeyDown(1) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(21, 0) < 0) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 8) and
            select(self.get(Fusssoldat_193).flags[30] == True) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(8)
                self.get(Strafing_219).values[18] = -1
            self.set_event_id(1048)
            if (PlayerKeyDown(8) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(21, 0) < 0) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 0) and
            select(self.get(Fusssoldat_193).flags[30] == True) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(0)
                self.get(Strafing_219).values[18] = -1
            self.set_event_id(1049)
            if (PlayerKeyDown(2) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(21, 0) < 0) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 24) and
            select(self.get(Fusssoldat_193).flags[30] == True) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(24)
                self.get(Strafing_219).values[18] = -1
            self.set_event_id(1050)
            if (PlayerKeyDown(4) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(21, 0) < 0) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 16) and
            select(self.get(Fusssoldat_193).flags[30] == True) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(16)
                self.get(Strafing_219).values[18] = -1
            self.set_event_id(1051)
            if (PlayerKeyDown(9) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 4) and
            select(self.get(Up2_418).values.get(0, 0) == 0) and
            select(self.get(Right2_419).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(4)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1052)
            if (PlayerKeyDown(9) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 4) and
            select(self.get(Up2_418).values.get(0, 0) == 1) and
            select(self.get(Right2_419).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(0)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1053)
            if (PlayerKeyDown(9) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 4) and
            select(self.get(Up2_418).values.get(0, 0) == 0) and
            select(self.get(Right2_419).values.get(0, 0) == 1) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(8)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1054)
            if (PlayerKeyDown(5) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 12) and
            select(self.get(Up2_418).values.get(0, 0) == 0) and
            select(self.get(Left2_421).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(12)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1055)
            if (PlayerKeyDown(5) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 12) and
            select(self.get(Up2_418).values.get(0, 0) == 1) and
            select(self.get(Left2_421).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(16)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1056)
            if (PlayerKeyDown(5) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 12) and
            select(self.get(Up2_418).values.get(0, 0) == 0) and
            select(self.get(Left2_421).values.get(0, 0) == 1) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(8)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1057)
            if (PlayerKeyDown(10) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 28) and
            select(self.get(Right2_419).values.get(0, 0) == 0) and
            select(self.get(Down2_420).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(28)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1058)
            if (PlayerKeyDown(10) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 28) and
            select(self.get(Right2_419).values.get(0, 0) == 1) and
            select(self.get(Down2_420).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(24)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1059)
            if (PlayerKeyDown(10) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 28) and
            select(self.get(Right2_419).values.get(0, 0) == 0) and
            select(self.get(Down2_420).values.get(0, 0) == 1) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(0)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1060)
            if (PlayerKeyDown(6) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 20) and
            select(self.get(Left2_421).values.get(0, 0) == 0) and
            select(self.get(Down2_420).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(20)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1061)
            if (PlayerKeyDown(6) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 20) and
            select(self.get(Left2_421).values.get(0, 0) == 1) and
            select(self.get(Down2_420).values.get(0, 0) == 0) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(24)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1062)
            if (PlayerKeyDown(6) and
            select(self.get(Fusssoldat_193).values.get(7, 0) == 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Strafing_219).values.get(18, 0) != 20) and
            select(self.get(Left2_421).values.get(0, 0) == 0) and
            select(self.get(Down2_420).values.get(0, 0) == 1) and
            self.not_always()):
                self.get(Strafing_219).movement.start()
                self.get(Strafing_219).movement.set_speed(9)
                self.get(Strafing_219).set_direction(16)
                self.get(Strafing_219).values[18] = -1
                self.get(Fusssoldat_193).flags[30] = False
            self.set_event_id(1063)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            negate(PlayerKeyDown(6)) and
            negate(PlayerKeyDown(10)) and
            negate(PlayerKeyDown(9)) and
            negate(PlayerKeyDown(5)) and
            self.not_always()):
                self.get(Fusssoldat_193).flags[30] = True
                self.get(Fusssoldat_193).values[21] = 1
            self.set_event_id(1068)
            if self.every(0.01):
                self.get(Fusssoldat_193).values[21] -= 1
            self.set_event_id(1069)
            if True:
                self.get(Active9_222).set_position(x = cos(self.get(Active9_222).values[1])*100+self.get(Fusssoldat_193).x)
                self.get(Active9_222).set_position(y = sin(self.get(Active9_222).values[1])*100+self.get(Fusssoldat_193).y)
                self.get(Fusssoldat_193).LookAt({'y': 0, 'x': 0, 'parent': 'self.get(Active9_222)'})
                self.get(FastMouse_252).subtract_value(3)
            self.set_event_id(1071)
            if (select(self.get(Strafing_219).IsOverlapping(qualifier_2)) and
            select(self.get(Strafing_219).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Fusssoldat_193).values[21] = 8
                self.get(Strafing_219).movement.stop()
                self.get(Strafing_219).set_position(x = self.get(TrackX_268).get_value())
                self.get(Strafing_219).set_position(y = self.get(TrackY_269).get_value())
                self.get(Strafing_219).values[18] = 'self.get(Strafing_219).GetDirection'
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
            self.set_event_id(1073)
            if select(self.get(Strafing_219).IsOverlapping(qualifier_3)):
                self.get(Fusssoldat_193).values[21] = 8
                self.get(Strafing_219).movement.stop()
                self.get(Strafing_219).set_position(x = self.get(TrackX_268).get_value())
                self.get(Strafing_219).set_position(y = self.get(TrackY_269).get_value())
                self.get(Strafing_219).values[18] = 'self.get(Strafing_219).GetDirection'
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
            self.set_event_id(1075)
            if (select(self.get(Strafing_219).IsOverlapping(qualifier_2)) and
            select(self.get(Strafing_219).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(qualifier_2).values.get(9, 0) >= self.get(Strafing_219).values[9]+2000)):
                self.get(qualifier_2).values[1] = 0
                self.get(Track_270).set_value(0)
            self.set_event_id(1076)
            if (select(self.get(Strafing_219).IsOverlapping(qualifier_2)) and
            select(self.get(Strafing_219).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(qualifier_2).values.get(9, 0) < self.get(Strafing_219).values[9]+2000)):
                self.get(qualifier_2).values[1] = 1
                self.get(Track_270).set_value(1)
            self.set_event_id(1077)
            if select(negate(self.get(Strafing_219).IsOverlapping(qualifier_2))):
                self.get(qualifier_2).values[1] = 0
                self.get(Track_270).set_value(0)
            self.set_event_id(1078)
            if (select(self.get(Strafing_219).IsOverlapping(qualifier_2)) and
            select(self.get(qualifier_2).values.get(1, 0) == 1) and
            select(self.get(Strafing_219).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Fusssoldat_193).values[21] = 8
                self.get(Strafing_219).movement.stop()
                self.get(Strafing_219).set_position(x = self.get(TrackX_268).get_value())
                self.get(Strafing_219).set_position(y = self.get(TrackY_269).get_value())
                self.get(qualifier_2).values[1] = 0
                self.get(Track_270).set_value(0)
                self.get(Strafing_219).values[18] = 'self.get(Strafing_219).GetDirection'
                self.get(Strafing_219).values[1] = 'self.get(Strafing_219).GetDirection'
            self.set_event_id(1079)
            if (select(self.get(Strafing_219).IsOverlapping(qualifier_2)) and
            select(self.get(qualifier_2).values.get(9, 0) >= self.get(Strafing_219).values[9])):
                self.get(TrackX_268).set_value(self.get(Strafing_219).x)
            self.set_event_id(1080)
            if (select(self.get(Strafing_219).IsOverlapping(qualifier_2)) and
            select(self.get(qualifier_2).values.get(9, 0) >= self.get(Strafing_219).values[9]) and
            select(self.get(Track_270).get_value() == 0)):
                self.get(TrackY_269).set_value(self.get(Strafing_219).y)
            self.set_event_id(1081)
            if (select(self.get(Fusssoldat_193).IsOverlapping(qualifier_2)) and
            select(negate(self.get(Strafing_219).IsOverlapping(qualifier_2))) and
            select(self.get(Strafing_219).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(TrackX_268).set_value(self.get(Strafing_219).x)
                self.get(TrackY_269).set_value(self.get(Strafing_219).y)
            self.set_event_id(1082)
            if select(negate(self.get(Strafing_219).IsOverlapping(qualifier_2))):
                self.get(TrackX_268).set_value(self.get(Strafing_219).x)
                self.get(TrackY_269).set_value(self.get(Strafing_219).y)
            self.set_event_id(1083)
            if select(self.get(Active9_222).values.get(1, 0) < 0):
                self.get(Active9_222).values[1] = 359
            self.set_event_id(1084)
            if select(self.get(Active9_222).values.get(1, 0) >= 360):
                self.get(Active9_222).values[1] = 0
            self.set_event_id(1085)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Up_227))) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Down_228))) and
            self.get(Active9_222).values[1] > 0 and
            self.get(Active9_222).values[1] < 180):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1086)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Up_227))) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Down_228))) and
            self.get(Active9_222).values[1] >= 180 and
            self.get(Active9_222).values[1] < 360):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1087)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Up_227))) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Down_228))) and
            self.get(Active9_222).values[1] > 180 and
            self.get(Active9_222).values[1] < 360):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1088)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Up_227))) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Down_228))) and
            self.get(Active9_222).values[1] >= 0 and
            self.get(Active9_222).values[1] < 180):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1089)
            if (select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.get(Active9_222).values[1] >= 90 and
            self.get(Active9_222).values[1] < 270):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1090)
            if (select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.get(Active9_222).values[1] > 270):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1091)
            if (select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.get(Active9_222).values[1] < 90):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1092)
            if (select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.get(Active9_222).values[1] > 90 and
            self.get(Active9_222).values[1] < 270):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1093)
            if (select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.get(Active9_222).values[1] >= 270):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1094)
            if (select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.get(Active9_222).values[1] < 90):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1095)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            self.get(Active9_222).values[1] >= 45 and
            self.get(Active9_222).values[1] < 225):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1096)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            self.get(Active9_222).values[1] > 225):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1097)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            self.get(Active9_222).values[1] < 45):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1098)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            self.get(Active9_222).values[1] >= 135 and
            self.get(Active9_222).values[1] < 315):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1099)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            self.get(Active9_222).values[1] > 315):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1100)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(self.get(Mouse2_229).IsOverlapping(Up_227)) and
            self.get(Active9_222).values[1] < 135):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1101)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            self.get(Active9_222).values[1] > 135 and
            self.get(Active9_222).values[1] <= 315):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1102)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            self.get(Active9_222).values[1] > 315):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1103)
            if (select(self.get(Mouse_224).IsOverlapping(Left_225)) and
            select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            self.get(Active9_222).values[1] < 135):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1104)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            self.get(Active9_222).values[1] > 45 and
            self.get(Active9_222).values[1] <= 225):
                self.get(Active9_222).values[1] -= 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100)
                self.get(DetectMouseChange_325).set_value(-1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1105)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            self.get(Active9_222).values[1] > 225):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1106)
            if (select(self.get(Mouse_224).IsOverlapping(Right_226)) and
            select(self.get(Mouse2_229).IsOverlapping(Down_228)) and
            self.get(Active9_222).values[1] < 45):
                self.get(Active9_222).AddToAlterable(1, 1+(((self.get(FastMouse_252).get_value()/4)*self.get(TurningSpeed_389).get_value())/100))
                self.get(DetectMouseChange_325).set_value(1)
                self.get(FastMouse_252).add_value(5)
            self.set_event_id(1107)
            if select(self.get(Mouse_224).IsOverlapping(Left_225)):
                self.get(Mouse_224).set_position(x = self.get(Mouse_224).x+3)
            self.set_event_id(1108)
            if select(self.get(Mouse_224).IsOverlapping(Right_226)):
                self.get(Mouse_224).set_position(x = self.get(Mouse_224).x-3)
            self.set_event_id(1109)
            if select(self.get(Mouse2_229).IsOverlapping(Up_227)):
                self.get(Mouse2_229).set_position(y = self.get(Mouse2_229).y+3)
            self.set_event_id(1110)
            if select(self.get(Mouse2_229).IsOverlapping(Down_228)):
                self.get(Mouse2_229).set_position(y = self.get(Mouse2_229).y-3)
            self.set_event_id(1111)
            if (select(negate(self.get(Mouse2_229).IsOverlapping(Up_227))) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Down_228))) and
            self.not_always()):
                self.get(Mouse2_229).set_position(y = 541)
            self.set_event_id(1112)
            if (select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.not_always()):
                self.get(Mouse_224).set_position(x = 229)
            self.set_event_id(1113)
            if (select(negate(self.get(Mouse2_229).IsOverlapping(Up_227))) and
            select(negate(self.get(Mouse2_229).IsOverlapping(Down_228))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Left_225))) and
            select(negate(self.get(Mouse_224).IsOverlapping(Right_226))) and
            self.not_always()):
                self.get(FastMouse_252).set_value(0)
            self.set_event_id(1114)
            if select(self.get(Mouse_224).MovementStopped()):
                self.get(Mouse_224).set_position(x = 229)
            self.set_event_id(1115)
            if select(self.get(Mouse2_229).MovementStopped()):
                self.get(Mouse2_229).set_position(y = 541)
            self.set_event_id(1116)
            if (select(self.get(DetectMouseChange_325).get_value() != self.get(SaveMouseChange_326).get_value()) and
            select(self.get(SaveMouseChange_326).get_value() != 0)):
                self.get(FastMouse_252).set_value(0)
            self.set_event_id(1117)
            if True:
                self.get(SaveMouseChange_326).set_value(self.get(DetectMouseChange_325).get_value())
                self.get(Up2_418).set_position(self.get(Strafing_219).x + 0, self.get(Strafing_219).x + -15) # {'y': -15, 'x': 0, 'parent': 'self.get(Strafing_219)'}
                self.get(Down2_420).set_position(self.get(Strafing_219).x + 0, self.get(Strafing_219).x + 12) # {'y': 12, 'x': 0, 'parent': 'self.get(Strafing_219)'}
                self.get(Right2_419).set_position(self.get(Strafing_219).x + 9, self.get(Strafing_219).x + 0) # {'y': 0, 'x': 9, 'parent': 'self.get(Strafing_219)'}
                self.get(Left2_421).set_position(self.get(Strafing_219).x + -7, self.get(Strafing_219).x + 0) # {'y': 0, 'x': -7, 'parent': 'self.get(Strafing_219)'}
        if False:#self.groups['Dead Reckoning']:
            self.set_event_id(1120)
            if True:
                self.get(Down2_420).values[9] = self.get(Down2_420).y*1000+self.get(Down2_420).x-10000
                self.get(Up2_418).values[9] = self.get(Up2_418).y*1000+self.get(Up2_418).x
                self.get(Right2_419).values[9] = self.get(Right2_419).y*1000+self.get(Right2_419).x
                self.get(Left2_421).values[9] = self.get(Left2_421).y*1000+self.get(Left2_421).x
            self.set_event_id(1121)
            if (select(self.get(Down2_420).IsOverlapping(qualifier_2)) and
            select(self.get(Down2_420).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(qualifier_2).values.get(9, 0) > self.get(Down2_420).values[9]+2000)):
                self.get(Down2_420).values[0] = 0
            self.set_event_id(1122)
            if (select(self.get(Down2_420).IsOverlapping(qualifier_2)) and
            select(self.get(Down2_420).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(qualifier_2).values.get(9, 0) <= self.get(Down2_420).values[9]+2000)):
                self.get(Down2_420).values[0] = 1
            self.set_event_id(1123)
            if (select(self.get(Up2_418).IsOverlapping(qualifier_2)) and
            select(self.get(Up2_418).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Up2_418).values[0] = 1
            self.set_event_id(1124)
            if (select(self.get(Up2_418).IsOverlapping(qualifier_2)) and
            select(self.get(Up2_418).values.get(9, 0) < self.get(qualifier_2).values[9])):
                self.get(Up2_418).values[0] = 0
            self.set_event_id(1125)
            if (select(self.get(Right2_419).IsOverlapping(qualifier_2)) and
            select(self.get(Right2_419).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Right2_419).values[0] = 1
            self.set_event_id(1126)
            if (select(self.get(Right2_419).IsOverlapping(qualifier_2)) and
            select(self.get(Right2_419).values.get(9, 0) < self.get(qualifier_2).values[9])):
                self.get(Right2_419).values[0] = 0
            self.set_event_id(1127)
            if (select(self.get(Left2_421).IsOverlapping(qualifier_2)) and
            select(self.get(Left2_421).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Left2_421).values[0] = 1
            self.set_event_id(1128)
            if (select(self.get(Left2_421).IsOverlapping(qualifier_2)) and
            select(self.get(Left2_421).values.get(9, 0) < self.get(qualifier_2).values[9])):
                self.get(Left2_421).values[0] = 0
            self.set_event_id(1129)
            if select(negate(self.get(Down2_420).IsOverlapping(qualifier_2))):
                self.get(Down2_420).values[0] = 0
            self.set_event_id(1130)
            if select(negate(self.get(Right2_419).IsOverlapping(qualifier_2))):
                self.get(Right2_419).values[0] = 0
            self.set_event_id(1131)
            if select(negate(self.get(Up2_418).IsOverlapping(qualifier_2))):
                self.get(Up2_418).values[0] = 0
            self.set_event_id(1132)
            if select(negate(self.get(Left2_421).IsOverlapping(qualifier_2))):
                self.get(Left2_421).values[0] = 0
            self.set_event_id(1133)
            if select(self.get(qualifier_7).OutsidePlayfield()):
                self.get(qualifier_7).values[0] = 1
            self.set_event_id(1134)
            if select(self.get(qualifier_7).IsOverlapping(qualifier_3)):
                self.get(qualifier_7).values[0] = 1
            self.set_event_id(1135)
            if (select(self.get(Fusssoldat2_194).IsOverlapping(qualifier_2)) and
            select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0]) and
            select(self.get(Fusssoldat2_194).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Head_441).force_animation('User defined 1')
            self.set_event_id(1136)
            if select(self.get(Head_441).IsOverlapping(qualifier_3)):
                self.get(Head_441).force_animation('User defined 1')
            self.set_event_id(1137)
            if select(self.get(Head_441).CompareY(3)):
                self.get(Head_441).force_animation('User defined 1')
            self.set_event_id(1138)
            if (select(negate(self.get(Head_441).IsOverlapping(qualifier_3))) and
            select(self.get(Head_441).values.get(0, 0) == self.get(Fusssoldat2_194).values[0]) and
            select(negate(self.get(Fusssoldat2_194).IsOverlapping(qualifier_2))) and
            select(self.get(Head_441).CompareY(3))):
                self.get(Head_441).force_animation('Stopped')
            self.set_event_id(1139)
            if (select(self.get(Fusssoldat2_194).IsOverlapping(qualifier_2)) and
            select(self.get(Fusssoldat2_194).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(Fusssoldat2_194).values.get(0, 0) == self.get(Head_441).values[0]) and
            False):
                self.get(Head_441).force_animation('Stopped')
            self.set_event_id(1143)
            if (select(self.get(Strafing2_220).IsOverlapping(qualifier_2)) and
            select(self.get(Strafing2_220).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(qualifier_2).values.get(9, 0) >= self.get(Strafing2_220).values[9]+2000)):
                self.get(Strafing2_220).values[19] = 0
            self.set_event_id(1144)
            if (select(self.get(Strafing2_220).IsOverlapping(qualifier_2)) and
            select(self.get(Strafing2_220).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(qualifier_2).values.get(9, 0) < self.get(Strafing2_220).values[9]+2000)):
                self.get(Strafing2_220).values[19] = 1
            self.set_event_id(1145)
            if select(negate(self.get(Strafing2_220).IsOverlapping(qualifier_2))):
                self.get(Strafing2_220).values[19] = 0
            self.set_event_id(1146)
            if (select(self.get(Strafing2_220).IsOverlapping(qualifier_2)) and
            select(self.get(Strafing2_220).values.get(19, 0) == 1) and
            select(self.get(Strafing2_220).values.get(23, 0) == 0) and
            select(self.get(Strafing2_220).values.get(24, 0) == 0) and
            select(self.get(Strafing2_220).values.get(9, 0) >= self.get(qualifier_2).values[9])):
                self.get(Strafing2_220).values[19] = 0
                self.get(Strafing2_220).values[4] = 0
                self.get(Strafing2_220).movement.stop()
            self.set_event_id(1150)
            if select(negate(self.get(Nade2_459).IsOverlapping(qualifier_2))):
                self.get(Nade2_459).values[19] = 0
            self.set_event_id(1151)
            if (select(self.get(Nade2_459).IsOverlapping(qualifier_2)) and
            select(self.get(Nade2_459).values.get(9, 0) < self.get(qualifier_2).values[9]) and
            select(self.get(qualifier_2).values.get(9, 0) < self.get(Nade2_459).values[9]+2000) and
            select(self.get(Nade2_459).values.get(19, 0) == 0)):
                self.get(Nade2_459).values[19] = -1
                self.get(Nade2_459).set_direction(32-'self.get(Nade2_459).GetDirection')
        if self.groups['W1']:
            self.set_event_id(1155)
            if self.players[0].lives > 1:
                self.groups['W1'] = False
        if self.groups['W2']:
            self.set_event_id(1173)
            if self.players[0].lives != 2:
                self.groups['W2'] = False
            self.set_event_id(1174)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 2 and
            select(self.get(AmmoCurrent_311).get_value() == 0) and
            select(self.get(Active5_213).NumberOfObjects(0)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.get(ShotLatence_230).set_value(12)
                SoundAutoPlay('empty.wav')
            self.set_event_id(1175)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 2 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
                self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 8, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 8, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 21
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 6, 1, 0)
                self.get(ShotLatence_230).set_value(12)
                self.get(Accuracy_238).add_value(14)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(AmmoCurrent_311).subtract_value(1)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(500):
                    if self.loop_waffe2(loop_index) == False: break
                SoundAutoPlay('ak47.wav')
        if self.groups['W3']:
            self.set_event_id(1191)
            if self.players[0].lives != 3:
                self.groups['W3'] = False
            self.set_event_id(1206)
            if (select(self.get(Strafing_219).values.get(5, 0) == 2) and
            select(self.get(Active7_195).NumberOfObjects(0))):
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Active7_195).values[0] = cos((self.get(Fusssoldat_193).values[18]-10))
                self.get(Active7_195).values[1] = sin((self.get(Fusssoldat_193).values[18]-10))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 21
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 6, 1, 0)
                self.get(ShotLatence_230).set_value(40)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(400):
                    if self.loop_waffe3(loop_index) == False: break
            self.set_event_id(1207)
            if (select(self.get(Strafing_219).values.get(5, 0) == 1) and
            select(self.get(Active7_195).NumberOfObjects(0))):
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Active7_195).values[0] = cos((self.get(Fusssoldat_193).values[18]+10))
                self.get(Active7_195).values[1] = sin((self.get(Fusssoldat_193).values[18]+10))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 21
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 6, 1, 0)
                self.get(ShotLatence_230).set_value(40)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(400):
                    if self.loop_waffe3(loop_index) == False: break
        if self.groups['W 4']:
            self.set_event_id(1211)
            if self.players[0].lives != 4:
                self.groups['W 4'] = False
        if self.groups['W 5']:
            self.set_event_id(1229)
            if self.players[0].lives != 5:
                self.groups['W 5'] = False
                self.get(Snipercounter_438).set_value(0)
            self.set_event_id(1230)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 5 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.get(Snipercounter_438).add_value(1)
                self.get(Accuracy_238).SetMinimumValue(immediate_compare('self.get(Strafing_219).Speed', '=', 0, 0, 30))
            self.set_event_id(1231)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 5 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False) and
            self.every(0.08)):
                self.get(Accuracy_238).subtract_value(immediate_compare('self.get(Strafing_219).Speed', '=', 0, 3, 0))
            self.set_event_id(1232)
            if negate(PlayerKeyDown(16)):
                self.get(Snipercounter_438).set_value(0)
            self.set_event_id(1234)
            if (select(self.get(Snipercounter_438).get_value() == 30) and
            self.players[0].lives == 5 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
                self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 1, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 1, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 120
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 13, 1, 0)
                self.get(ShotLatence_230).set_value(50)
                self.get(Accuracy_238).add_value(50)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(AmmoCurrent_311).subtract_value(1)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(800):
                    if self.loop_waffe5(loop_index) == False: break
                self.get(Snipercounter_438).set_value(0)
                SoundAutoPlay('sniper.wav')
        if self.groups['W 6']:
            self.set_event_id(1250)
            if self.players[0].lives != 6:
                self.groups['W 6'] = False
            self.set_event_id(1251)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 6 and
            select(self.get(AmmoCurrent_311).get_value() == 0) and
            select(self.get(Active5_213).NumberOfObjects(0)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.get(ShotLatence_230).set_value(15)
                SoundAutoPlay('empty.wav')
            self.set_event_id(1252)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 6 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
                self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 14, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 14, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 18
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 6, 1, 0)
                self.get(ShotLatence_230).set_value(15)
                self.get(Accuracy_238).add_value(14)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(AmmoCurrent_311).subtract_value(1)
                self.get(Rauch_197).force_animation('User defined 1')
                self.get(Fusssoldat_193).values[2] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(450):
                    if self.loop_waffe6(loop_index) == False: break
                SoundAutoPlay('mp5.wav')
        if self.groups['W 7']:
            self.set_event_id(1268)
            if self.players[0].lives != 7:
                self.groups['W 7'] = False
            self.set_event_id(1269)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 7 and
            select(self.get(AmmoCurrent_311).get_value() == 0) and
            select(self.get(Active5_213).NumberOfObjects(0)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.get(ShotLatence_230).set_value(22)
                SoundAutoPlay('empty.wav')
            self.set_event_id(1270)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 7 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
                self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 13, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 13, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 33
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 6, 1, 0)
                self.get(ShotLatence_230).set_value(22)
                self.get(Accuracy_238).add_value(27)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(AmmoCurrent_311).subtract_value(1)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(500):
                    if self.loop_waffe7(loop_index) == False: break
                SoundAutoPlay('g3.wav')
        if self.groups['W 8']:
            self.set_event_id(1286)
            if self.players[0].lives != 8:
                self.groups['W 8'] = False
        if self.groups['W 9']:
            self.set_event_id(1304)
            if self.players[0].lives != 9:
                self.groups['W 9'] = False
            self.set_event_id(1305)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 9 and
            select(self.get(AmmoCurrent_311).get_value() == 0) and
            select(self.get(Active5_213).NumberOfObjects(0)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.get(ShotLatence_230).set_value(14)
                SoundAutoPlay('empty.wav')
            self.set_event_id(1306)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 9 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
                self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 14, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 14, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 28
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 5, 1, 0)
                self.get(ShotLatence_230).set_value(14)
                self.get(Accuracy_238).add_value(22)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(AmmoCurrent_311).subtract_value(1)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(500):
                    if self.loop_waffe9(loop_index) == False: break
                SoundAutoPlay('m4.wav')
        if self.groups['W 10']:
            self.set_event_id(1322)
            if self.players[0].lives != 10:
                self.groups['W 10'] = False
            self.set_event_id(1323)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 10 and
            select(self.get(AmmoCurrent_311).get_value() == 0) and
            select(self.get(Active5_213).NumberOfObjects(0)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.get(ShotLatence_230).set_value(12)
                SoundAutoPlay('empty.wav')
            self.set_event_id(1324)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 10 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
                self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 5, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 5, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 23
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 4, 1, 0)
                self.get(ShotLatence_230).set_value(12)
                self.get(Accuracy_238).add_value(17)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(AmmoCurrent_311).subtract_value(1)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(450):
                    if self.loop_waffe10(loop_index) == False: break
                SoundAutoPlay('galil.wav')
        if self.groups['W 11']:
            self.set_event_id(1340)
            if self.players[0].lives != 11:
                self.groups['W 11'] = False
            self.set_event_id(1341)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 11 and
            select(self.get(AmmoCurrent_311).get_value() == 0) and
            select(self.get(Active5_213).NumberOfObjects(0)) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.get(ShotLatence_230).set_value(16)
                SoundAutoPlay('empty.wav')
            self.set_event_id(1342)
            if (PlayerKeyDown(16) and
            self.players[0].lives == 11 and
            select(self.get(AmmoCurrent_311).get_value() >= 1) and
            select(self.get(Fusssoldat_193).values.get(14, 0) == 1) and
            select(self.get(ShotLatence_230).get_value() == 0) and
            select(self.get(Active7_195).NumberOfObjects(0)) and
            select(self.get(Strafing_219).flags[9] == False)):
                self.create_object(ActiveObject1_218, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'y': 0, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'ActiveObject1_218'}
                self.get(Fusssoldat_193).Shoot({'shoot_speed': 7, 'parent': 'self.get(Fusssoldat_193)', 'use_action_point': True, 'use_direction': True, 'shoot_object': 'Rauch_197', 'y': 0, 'x': 0})
                self.create_object(TestShoot_306, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 4) # {'y': 4, 'use_action_point': True, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'TestShoot_306'}
                self.create_object(Active7_195, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 0) # {'parent': 'self.get(Fusssoldat_193)', 'create_object': 'Active7_195', 'transform_position_direction': True, 'use_direction': True, 'use_action_point': True, 'y': 0, 'x': 0}
                self.get(Fusssoldat_193).values[17] = 2*randrange(2)-1
                self.get(Active7_195).values[0] = cos((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 7, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[1] = sin((self.get(Active9_222).values[1]+(immediate_compare(self.get(Accuracy_238).get_value(), '>', 7, 1, 0)*self.get(Fusssoldat_193).values[17]*randrange(self.get(Accuracy_238).get_value()))))
                self.get(Active7_195).values[23] = self.get(Active7_195).x
                self.get(Active7_195).values[24] = self.get(Active7_195).y
                self.get(Active7_195).values[3] = 27
                self.get(Active7_195).values[14] = immediate_compare(randrange(self.get(Accuracy_238).get_value()), '>', 5, 1, 0)
                self.get(ShotLatence_230).set_value(16)
                self.get(Accuracy_238).add_value(20)
                self.get(Active7_195).values[9] = self.get(Active7_195).y*1000
                self.get(TestShoot_306).set_visible(False)
                self.get(AmmoCurrent_311).subtract_value(1)
                self.get(Fusssoldat_193).values[2] = 0
                self.get(ActiveObject1_218).set_position(x = self.get(ActiveObject1_218).x+(randrange(5)-2))
                self.get(ActiveObject1_218).set_position(y = self.get(ActiveObject1_218).y+(randrange(3)-1))
                self.get(Rauch_197).values[9] = 999888
                self.get(Active7_195).values[7] = self.get(Active9_222).values[7]
                for loop_index in xrange(800):
                    if self.loop_waffe11(loop_index) == False: break
                SoundAutoPlay('svd.wav')
        if self.groups['W 12']:
            self.set_event_id(1358)
            if self.players[0].lives != 12:
                self.groups['W 12'] = False
        if self.groups['Disconnect']:
            self.set_event_id(1376)
            if True:
                self.get(Fusssoldat2_194).SpreadValue(21, 0, 0)
            self.set_event_id(1377)
            if self.check_once():
                self.get(ScoreBoard_231).reset()
                self.get(ScoreBar_234).set_visible(False)
                self.get(NameScore_235).destroy()
                self.get(FragsScore_236).destroy()
                self.get(IdScore_237).destroy()
                self.get(IdPing_307).destroy()
                self.get(NameScore2_347).destroy()
                self.get(FragsScore2_348).destroy()
                self.get(IdScore2_349).destroy()
                self.get(IdPing2_350).destroy()
                self.get(NameScore3_351).destroy()
                self.get(FragsScore3_352).destroy()
                self.get(IdScore3_353).destroy()
                self.get(IdPing3_354).destroy()
                self.get(Players_317).set_visible(False)
                self.get(PlOnlineText_316).set_visible(False)
            self.set_event_id(1378)
            if self.check_once():
                self.get(ScoreBoard_231).add_line(str(self.get(Frags_209).get_value())+','+self.get(RealName_390).text+','+str(self.get(VisibleId_424).get_value())+','+str(self.get(Ping_233).get_value())+','+str(self.get(Deaths_210).get_value())+',1')
                self.get(ScoreBar_234).set_visible(True)
                self.get(NameScore_235).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore_236).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore_237).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing_307).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore2_347).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore2_348).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore2_349).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing2_350).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(NameScore3_351).DisplayText({'y': 158, 'x': 232, 'create_object': 'qualifier_2047'}, 0)
                self.get(FragsScore3_352).DisplayText({'y': 158, 'x': 363, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdScore3_353).DisplayText({'y': 158, 'x': 439, 'create_object': 'qualifier_2047'}, 0)
                self.get(IdPing3_354).DisplayText({'y': 158, 'x': 504, 'create_object': 'qualifier_2047'}, 0)
                self.get(Players_317).set_value('self.get(Fusssoldat2_194).ObjectCount'+1)
                self.get(PlOnlineText_316).set_visible(True)
                self.get(Players_317).set_visible(True)
                for loop_index in xrange('self.get(Fusssoldat2_194).ObjectCount'):
                    if self.loop_entry(loop_index) == False: break
                for loop_index in xrange('self.get(ScoreBoard_231).ListGetLineCount'):
                    if self.loop_list(loop_index) == False: break
            self.set_event_id(1379)
            if mid_string(self.get(ErrorMsg_244).text, 0, 1) == '*':
                self.add_hud_line('Disconnected - Reason: '+mid_string(self.get(ErrorMsg_244).text, 1, 200))
                self.groups['Game'] = False
                self.get(Fusssoldat2_194).destroy()
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Fusssoldat_193).movement.stop()
                self.get(Rauch_197).destroy()
                self.players[0].set_ignore(True)
                self.get(Active7_195).destroy()
                self.get(Splitter_202).destroy()
                self.get(AmmoPack_208).destroy()
                self.get(MagicExplode3_212).destroy()
                self.get(NameTag2_429).destroy()
                self.get(Active5_213).destroy()
                self.get(Nade_458).destroy()
                self.get(Gaswolke_215).destroy()
                self.get(Exp_247).destroy()
                self.groups['Disconnect'] = False
                self.groups['Chat'] = False
                self.groups['Join Team'] = False
                self.get(Chatting_355).destroy()
                self.get(ChattingPlayer_356).destroy()
                self.get(C4_374).destroy()
                self.get(Nade2_459).destroy()
                self.get(PlShadow2_383).destroy()
                self.get(GrenadeSpot_398).destroy()
                self.get(Moo_181).disconnect()
                self.get(NameTag3_433).destroy()
                self.get(Chat_204).set_value('')
                self.get(Chat_204).EditMakeInvisible()
                self.get(Chat_204).set_focus(False)
                self.get(Molotov_450).destroy()
                self.get(Active17_451).destroy()
                self.get(P1_452).destroy()
                self.get(FlameDmg_456).destroy()
                self.get(BigflameDmg_457).destroy()
                self.get(SmokeExp_460).destroy()
        if self.groups['Crates']:
            self.set_event_id(1382)
            if (self.every(3.0) and
            len(self.get(AmmoPack_208, True)) <= len(self.get(Fusssoldat2_194, True))+2 and
            select(self.get(DM_412).get_value() == 1) and
            select(self.get(Respawn_201).get_value() < 6)):
                self.create_object(AmmoTest_319, -74, 245) # {'y': 245, 'x': -74, 'create_object': 'AmmoTest_319'}
                self.get(AmmoTest_319).set_visible(False)
                self.get(AmmoTest_319).set_position(x = randrange(750)+26)
                self.get(AmmoTest_319).set_position(y = randrange(525)+50)
            self.set_event_id(1385)
            for item in self.get(AmmoTest_319, True):
                if item.values.get(0, 0) >= 2:
                    pack = self.create_object(AmmoPack_208, item.x + 0, item.x + 0) # {'y': 0, 'x': 0, 'parent': 'self.get(AmmoTest_319)', 'create_object': 'AmmoPack_208'}
                    item.destroy()
                    pack.values[9] = 1000+pack.y
                    pack.BringToBack()
                    self.get(NotID_430).set_value(0)
                    self.get(Msg_427).set_value('207'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+str((self.get(AmmoPack_208).x+self.get(AmmoPack_208).y*1000+'self.get(AmmoPack_208).GetDirection'*1000000))+'00'+str(self.get(Csm_432).get_value()))
                    self.function_sendall()
                    self.function_csmup()
            self.set_event_id(1386)
            if self.every(1.0):
                for item in self.get(AmmoPack_208, True):
                    item.values[0] += 1
                for item in self.get(AmmoTest_319, True):
                    item.values[0] += 1
            self.set_event_id(1387)
            for item in self.get(AmmoPack_208, True):
                if item.values.get(0, 0) >= 40:
                    item.destroy()
        if self.groups['Msg']:
            self.set_event_id(1390)
            if self.every(1.0):
                self.get(MsgCounter_332).subtract_value(1)
            self.set_event_id(1391)
            if select(self.get(MsgCounter_332).get_value() == 0):
                self.get(ChangeMap_217).set_visible(False)
                self.get(ChangeMap_217).set_value('')
                self.groups['Msg'] = False
        if self.groups['Join Team']:
            self.set_event_id(1394)
            if (Qt.Key_1 in self.scene.key_presses and
            select(self.get(DM_412).get_value() == 0) and
            negate(self.groups['Chat'])):
                self.get(Killed_203).set_value('Waiting for new round')
                self.get(Killed_203).set_visible(True)
            self.set_event_id(1395)
            if (Qt.Key_2 in self.scene.key_presses and
            select(self.get(DM_412).get_value() == 0) and
            negate(self.groups['Chat'])):
                self.get(Killed_203).set_value('Waiting for new round')
                self.get(Killed_203).set_visible(True)
            self.set_event_id(1396)
            if (Qt.Key_1 in self.scene.key_presses and
            select(self.get(DM_412).get_value() == 1) and
            negate(self.groups['Chat'])):
                self.get(Respawn_201).set_value(5)
                self.get(String2_200).set_visible(True)
                self.get(Respawn_201).set_visible(True)
            self.set_event_id(1397)
            if (Qt.Key_2 in self.scene.key_presses and
            select(self.get(DM_412).get_value() == 1) and
            negate(self.groups['Chat'])):
                self.get(Respawn_201).set_value(5)
                self.get(String2_200).set_visible(True)
                self.get(Respawn_201).set_visible(True)
            self.set_event_id(1398)
            if (Qt.Key_1 in self.scene.key_presses and
            self.get_global_value(1) == 1 and
            negate(self.groups['Chat'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
            self.set_event_id(1399)
            if (Qt.Key_2 in self.scene.key_presses and
            self.get_global_value(1) == 1 and
            negate(self.groups['Chat'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
            self.set_event_id(1400)
            if (Qt.Key_1 in self.scene.key_presses and
            self.get_global_value(1) == 0 and
            negate(self.groups['Chat'])):
                self.get(Fusssoldat_193).values[8] = 1
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'police'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(1401)
            if (Qt.Key_2 in self.scene.key_presses and
            self.get_global_value(1) == 0 and
            negate(self.groups['Chat'])):
                self.get(Fusssoldat_193).values[8] = 2
                self.get(Police_342).set_visible(False)
                self.get(Terror_343).set_visible(False)
                self.get(Fusssoldat_193).values[14] = 0
                self.groups['Join Team'] = False
                self.get(NotID_430).set_value(0)
                self.get(Msg_427).set_value('213'+immediate_compare(self.get(VisibleId_424).get_value(), '<', 10, '0'+str(self.get(VisibleId_424).get_value()), str(self.get(VisibleId_424).get_value()))+'terror'+str(self.get(Csm_432).get_value()))
                self.function_sendall()
                self.function_csmup()
            self.set_event_id(1402)
            if True:
                self.get(Fusssoldat_193).values[8] = 0
        if self.groups['reset standard']:
            self.set_event_id(1405)
            if (select(self.get(SecondWeapon_318).get_value() > 0) and
            self.players[0].lives == 1):
                self.players[0].lives = self.get(SecondWeapon_318).get_value()
                self.get(Ammo1_321).set_value(15)
                self.get(AmmoCurrent_311).set_value(self.get(Ammo2_322).get_value())
                self.get(AmmoFull_312).set_value(self.get(Reload2_323).get_value())
                self.groups['Weapon Change Normal'] = True
                self.get(Active5_213).destroy()
                self.groups['Reload'] = False
                self.groups['reset standard'] = False
            self.set_event_id(1406)
            if (select(self.get(SecondWeapon_318).get_value() > 0) and
            self.players[0].lives == 8):
                self.players[0].lives = self.get(SecondWeapon_318).get_value()
                self.get(Ammo1_321).set_value(13)
                self.get(AmmoCurrent_311).set_value(self.get(Ammo2_322).get_value())
                self.get(AmmoFull_312).set_value(self.get(Reload2_323).get_value())
                self.groups['Weapon Change Normal'] = True
                self.get(Active5_213).destroy()
                self.groups['Reload'] = False
                self.groups['reset standard'] = False
            self.set_event_id(1407)
            if (select(self.get(SecondWeapon_318).get_value() == 0) and
            self.players[0].lives == 1):
                self.get(Ammo1_321).set_value(15)
                self.get(AmmoCurrent_311).set_value(15)
                self.groups['reset standard'] = False
            self.set_event_id(1408)
            if (select(self.get(SecondWeapon_318).get_value() == 0) and
            self.players[0].lives == 8):
                self.get(Ammo1_321).set_value(13)
                self.get(AmmoCurrent_311).set_value(13)
                self.groups['reset standard'] = False
            self.set_event_id(1409)
            if (select(self.get(SecondWeapon_318).get_value() > 0) and
            self.players[0].lives != 1 and
            self.players[0].lives != 8 and
            self.get_global_value(9) == 0):
                self.get(Ammo1_321).set_value(15)
                self.groups['reset standard'] = False
            self.set_event_id(1410)
            if (select(self.get(SecondWeapon_318).get_value() > 0) and
            self.players[0].lives != 1 and
            self.players[0].lives != 8 and
            self.get_global_value(9) == 1):
                self.get(Ammo1_321).set_value(13)
                self.groups['reset standard'] = False
        if self.groups['Shop']:
            self.set_event_id(1413)
            if (Qt.Key_1 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[4] == True) and
            select(self.get(SecondWeapon_318).get_value() != 4) and
            select(self.get(Money_366).get_value() >= 1200) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(1200)
                self.players[0].lives = 4
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-1200))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1414)
            if (Qt.Key_2 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[3] == True) and
            select(self.get(SecondWeapon_318).get_value() != 3) and
            select(self.get(Money_366).get_value() >= 1300) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(1300)
                self.players[0].lives = 3
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-1300))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1415)
            if (Qt.Key_3 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[6] == True) and
            select(self.get(SecondWeapon_318).get_value() != 6) and
            select(self.get(Money_366).get_value() >= 1500) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(1500)
                self.players[0].lives = 6
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-1500))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1416)
            if (Qt.Key_4 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[10] == True) and
            select(self.get(SecondWeapon_318).get_value() != 10) and
            select(self.get(Money_366).get_value() >= 2000) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(2000)
                self.players[0].lives = 10
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-2000))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1417)
            if (Qt.Key_5 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[11] == True) and
            select(self.get(SecondWeapon_318).get_value() != 11) and
            select(self.get(Money_366).get_value() >= 2300) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(2300)
                self.players[0].lives = 11
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-2300))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1418)
            if (Qt.Key_6 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[2] == True) and
            select(self.get(SecondWeapon_318).get_value() != 2) and
            select(self.get(Money_366).get_value() >= 2000) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(2000)
                self.players[0].lives = 2
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-2000))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1419)
            if (Qt.Key_7 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[9] == True) and
            select(self.get(SecondWeapon_318).get_value() != 9) and
            select(self.get(Money_366).get_value() >= 2500) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(2500)
                self.players[0].lives = 9
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-2500))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1420)
            if (Qt.Key_8 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[7] == True) and
            select(self.get(SecondWeapon_318).get_value() != 7) and
            select(self.get(Money_366).get_value() >= 2800) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(2800)
                self.players[0].lives = 7
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-2800))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1421)
            if (Qt.Key_9 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[12] == True) and
            select(self.get(SecondWeapon_318).get_value() != 12) and
            select(self.get(Money_366).get_value() >= 3000) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(3000)
                self.players[0].lives = 12
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-3000))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1422)
            if (Qt.Key_0 in self.scene.key_presses and
            select(self.get(Fusssoldat_193).flags[5] == True) and
            select(self.get(SecondWeapon_318).get_value() != 5) and
            select(self.get(Money_366).get_value() >= 3800) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(3800)
                self.players[0].lives = 5
                self.get(SecondWeapon_318).set_value('PlayerLives')
                self.groups['Weapon Change'] = True
                self.function_write_shop()
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-3800))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1423)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 4) and
            select(self.get(Money_366).get_value() >= 40) and
            select(self.get(AmmoFull_312).get_value() <= 6) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(40)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-40))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1424)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 3) and
            select(self.get(Money_366).get_value() >= 60) and
            select(self.get(AmmoFull_312).get_value() <= 4) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(60)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-60))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1425)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 6) and
            select(self.get(Money_366).get_value() >= 50) and
            select(self.get(AmmoFull_312).get_value() <= 3) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(50)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-50))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1426)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 2) and
            select(self.get(Money_366).get_value() >= 75) and
            select(self.get(AmmoFull_312).get_value() <= 3) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(75)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-75))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1427)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 9) and
            select(self.get(Money_366).get_value() >= 75) and
            select(self.get(AmmoFull_312).get_value() <= 3) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(75)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-75))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1428)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 7) and
            select(self.get(Money_366).get_value() >= 100) and
            select(self.get(AmmoFull_312).get_value() <= 2) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(100)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-100))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1429)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 5) and
            select(self.get(Money_366).get_value() >= 30) and
            select(self.get(AmmoFull_312).get_value() <= 7) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(30)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-30))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1430)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 10) and
            select(self.get(Money_366).get_value() >= 50) and
            select(self.get(AmmoFull_312).get_value() <= 4) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(50)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-50))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1431)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 11) and
            select(self.get(Money_366).get_value() >= 80) and
            select(self.get(AmmoFull_312).get_value() <= 4) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(80)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-80))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1432)
            if (Qt.Key_A in self.scene.key_presses and
            select(self.get(SecondWeapon_318).get_value() == 12) and
            select(self.get(Money_366).get_value() >= 75) and
            select(self.get(AmmoFull_312).get_value() <= 4) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(75)
                self.get(AmmoFull_312).add_value(1)
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-75))
                SoundAutoPlay('ammo.wav')
            self.set_event_id(1433)
            if (Qt.Key_Q in self.scene.key_presses and
            select(self.get(Fusssoldat_193).values.get(12, 0) != 3) and
            select(self.get(Money_366).get_value() >= 400) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(400)
                self.get(Fusssoldat_193).values[12] = 3
                self.groups['Grenades'] = True
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-400))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1434)
            if (Qt.Key_W in self.scene.key_presses and
            select(self.get(Fusssoldat_193).values.get(12, 0) != 1) and
            select(self.get(Money_366).get_value() >= 200) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(200)
                self.get(Fusssoldat_193).values[12] = 1
                self.groups['Grenades'] = True
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-200))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1435)
            if (Qt.Key_E in self.scene.key_presses and
            select(self.get(Fusssoldat_193).values.get(12, 0) != 2) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
            select(self.get(Money_366).get_value() >= 350) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(350)
                self.get(Fusssoldat_193).values[12] = 2
                self.groups['Grenades'] = True
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-350))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1436)
            if (Qt.Key_E in self.scene.key_presses and
            select(self.get(Fusssoldat_193).values.get(12, 0) != 4) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
            select(self.get(Money_366).get_value() >= 350) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(350)
                self.get(Fusssoldat_193).values[12] = 4
                self.groups['Grenades'] = True
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-350))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1437)
            if (Qt.Key_S in self.scene.key_presses and
            select(self.get(Fusssoldat_193).values.get(12, 0) != 5) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 2) and
            select(self.get(Money_366).get_value() >= 700) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(700)
                self.get(Fusssoldat_193).values[12] = 5
                self.groups['Grenades'] = True
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-700))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1438)
            if (Qt.Key_S in self.scene.key_presses and
            select(self.get(Fusssoldat_193).values.get(12, 0) != 6) and
            select(self.get(Fusssoldat_193).values.get(8, 0) == 1) and
            select(self.get(Money_366).get_value() >= 300) and
            negate(self.groups['Chat'])):
                self.get(Money_366).subtract_value(300)
                self.get(Fusssoldat_193).values[12] = 6
                self.groups['Grenades'] = True
                self.get(String31_437).set_value(str(to_number(self.get(String31_437).text)-300))
                SoundAutoPlay('collect.wav')
            self.set_event_id(1439)
            if (Qt.Key_Space in self.scene.key_presses and
            negate(self.groups['Chat'])):
                RestoreControls()
                self.get(Fusssoldat_193).values[7] = 1
                self.get(Strafing_219).movement.stop()
                self.get(ShopList_370).set_visible(False)
                self.get(ShopListPrice_371).set_visible(False)
                self.groups['Shop'] = False
                self.get(Shop1Blitter_372).set_visible(False)
                self.get(Shop2Blitter_373).set_visible(False)
                self.get(Shop1Blitter2_385).set_visible(False)
                self.get(Shop1Blitter3_386).set_visible(False)
            self.set_event_id(1440)
            if True:
                self.players[0].set_ignore(True)
                self.get(Fusssoldat_193).values[7] = 0
                self.get(Strafing_219).movement.stop()
        if self.groups['Backfix']:
            print 'backfix'
            self.set_event_id(1443)
            if (self.check_once() and
            self.get_global_value(1) == 0):
                self.groups['Connect'] = True
            self.set_event_id(1444)
            self.get(OverlayRedux_378).set_transparency(50)
            self.get(OverlayRedux_378).destroy()
            self.groups['Backfix'] = False
        if self.groups['Flashed']:
            self.set_event_id(1447)
            if select(self.get(FlashScreen_384).NumberOfObjects(0)):
                self.create_object(FlashScreen_384, 0, 0) # {'y': 0, 'x': 0, 'create_object': 'FlashScreen_384'}
                self.get(FlashScreen_384).ActivePictureCreateBackdrop('flash.jpg')
                self.get(FlashScreen_384).ActivePictureSetTransparency(immediate_compare(self.get(FlashTime_381).get_value(), '>', 99, 0, 100-self.get(FlashTime_381).get_value()))
                self.get(FlashScreen_384).values[9] = 20000000
                self.get(XtraXtraCRC_182).calculate(os.path.splitdrive(os.getcwd())[0]+(os.path.splitdrive(os.getcwd())[1]+'\\')+'flash.jpg')
                self.get(CheckFlash_387).set_value(self.get(XtraXtraCRC_182).get_crc())
            self.set_event_id(1448)
            if select(self.get(CheckFlash_387).get_value() != -636816703):
                self.get(ErrorMsg_244).set_value('Flash error')
                self.groups['Flashed'] = False
                self.groups['Disconnect'] = True
            self.set_event_id(1449)
            if self.every(0.02):
                self.get(FlashTime_381).subtract_value(1)
            self.set_event_id(1450)
            if select(self.get(FlashTime_381).get_value() == 0):
                self.groups['Flashed'] = False
                self.get(FlashScreen_384).destroy()
            self.set_event_id(1451)
            if self.every(0.04):
                self.get(Accuracy_238).add_value(1)
                self.get(FlashScreen_384).ActivePictureSetTransparency(immediate_compare(self.get(FlashTime_381).get_value(), '>', 99, 0, 100-self.get(FlashTime_381).get_value()))
        if self.groups['User left']:
            self.set_event_id(1454)
            if (self.every(1.0) and
            self.get(Players_317).get_value() == 'self.get(Fusssoldat2_194).ObjectCount'+1):
                for loop_index in xrange(self.get(Players_317).get_value()):
                    if self.loop_team_count(loop_index) == False: break
                self.groups['User left'] = False
        if self.groups['Graphic reduced']:
            self.set_event_id(1457)
            if True:
                self.get(Flashbang2_379).set_effect('None')
                self.get(Exp_247).set_effect('None')
                self.get(Gaswolke_215).set_effect('None')
                self.get(P1_452).set_effect('None')
                self.get(Explode_453).set_effect('None')
            self.set_event_id(1458)
            if select(self.get(Active2_254).values.get(0, 0) > 150):
                self.get(Active2_254).destroy()
            self.set_event_id(1459)
            if select(self.get(qualifier_8).values.get(0, 0) >= 25):
                self.get(qualifier_8).destroy()
        if self.groups['Graphic reduced 2']:
            self.set_event_id(1462)
            if True:
                self.get(ActiveObject1_218).destroy()
                self.get(Flashbang2_379).set_effect('None')
                self.get(Exp_247).set_effect('None')
                self.get(Gaswolke_215).set_effect('None')
                self.get(Active17_451).set_effect('None')
                self.get(P1_452).set_effect('None')
                self.get(Explode_453).set_effect('None')
            self.set_event_id(1469)
            if select(self.get(Active2_254).values.get(0, 0) > 60):
                self.get(Active2_254).destroy()
        if self.groups['Graphic reduced 3']:
            self.set_event_id(1472)
            if True:
                self.get(ActiveObject1_218).destroy()
                self.get(Flashbang2_379).set_effect('None')
                self.get(Exp_247).set_effect('None')
                self.get(Gaswolke_215).set_effect('None')
                self.get(Active2_254).destroy()
                self.get(Active17_451).set_effect('None')
                self.get(P1_452).set_effect('None')
                self.get(Explode_453).set_effect('None')
        if self.groups['Change team respawn dm']:
            self.set_event_id(1481)
            if select(self.get(Active17_451).values.get(1, 0) == self.get(VisibleId_424).get_value()):
                self.get(Active17_451).destroy()
            self.set_event_id(1482)
            if select(self.get(P1_452).values.get(1, 0) == self.get(VisibleId_424).get_value()):
                self.get(P1_452).destroy()
            self.set_event_id(1483)
            if select(self.get(FlameDmg_456).values.get(1, 0) == self.get(VisibleId_424).get_value()):
                self.get(FlameDmg_456).destroy()
            self.set_event_id(1484)
            if select(self.get(BigflameDmg_457).values.get(2, 0) == self.get(VisibleId_424).get_value()):
                self.get(BigflameDmg_457).destroy()
            self.set_event_id(1485)
            if select(self.get(Gaswolke_215).values.get(1, 0) == self.get(VisibleId_424).get_value()):
                self.get(Gaswolke_215).destroy()
            self.set_event_id(1486)
            if select(self.get(Nade_458).values.get(2, 0) == self.get(VisibleId_424).get_value()):
                self.get(Nade_458).destroy()
            self.set_event_id(1487)
            if select(self.get(Molotov_450).values.get(2, 0) == self.get(VisibleId_424).get_value()):
                self.get(Molotov_450).destroy()
            self.set_event_id(1488)
            if select(self.get(C4_374).values.get(2, 0) == self.get(VisibleId_424).get_value()):
                self.get(C4_374).destroy()
            self.set_event_id(1489)
            if select(self.get(Exp_247).values.get(2, 0) == self.get(VisibleId_424).get_value()):
                self.get(Exp_247).destroy()
            self.set_event_id(1490)
            if select(self.get(DM_412).get_value() == 1):
                self.get(Respawn_201).set_value(5)
                self.get(Respawn_201).set_visible(True)
                self.get(String2_200).set_visible(True)
                self.groups['Change team respawn dm'] = False
            self.set_event_id(1491)
            if select(self.get(DM_412).get_value() != 1):
                self.groups['Change team respawn dm'] = False
        if self.groups['Connect']:
            self.set_event_id(1494)
            if self.check_once():
                self.get(Moo_181).connect(self.get(Ip_46).text, to_number(self.get(Port_47).text))
                self.groups['Connect'] = False
        if self.groups['Speed Hack']:
            self.set_event_id(1499)
            if self.every(0.1):
                self.get(Cp2c_436).add_value(1)
        if self.groups['Footsteps']:
            self.set_event_id(1502)
            if (select(self.get(Fusssoldat2_194).values.get(4, 0) > 3) and
            select(self.get(Fusssoldat2_194).values.get(10, 0) <= 0) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y+14, 0, 0, 0))):
                self.get(Fusssoldat2_194).values[10] = 15
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('gravel'+str(randrange(4)+1)+'.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1503)
            if (select(self.get(Fusssoldat2_194).values.get(4, 0) > 3) and
            select(self.get(Fusssoldat2_194).values.get(10, 0) <= 0) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y+14, 192, 192, 192))):
                self.get(Fusssoldat2_194).values[10] = 15
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('street'+str(randrange(5)+1)+'.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1504)
            if (select(self.get(Fusssoldat2_194).values.get(4, 0) > 3) and
            select(self.get(Fusssoldat2_194).values.get(10, 0) <= 0) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y+14, 128, 128, 0))):
                self.get(Fusssoldat2_194).values[10] = 15
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('wood'+str(randrange(4)+1)+'.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1505)
            if (select(self.get(Fusssoldat2_194).values.get(4, 0) > 3) and
            select(self.get(Fusssoldat2_194).values.get(10, 0) <= 0) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y+14, 0, 255, 0))):
                self.get(Fusssoldat2_194).values[10] = 15
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('grass'+str(randrange(4)+1)+'.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1506)
            if (select(self.get(Fusssoldat2_194).values.get(4, 0) > 3) and
            select(self.get(Fusssoldat2_194).values.get(10, 0) <= 0) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y+14, 0, 0, 255))):
                self.get(Fusssoldat2_194).values[10] = 15
                self.create_object(OverlayRedux2_443, self.get(Fusssoldat2_194).x + 0, self.get(Fusssoldat2_194).x + 20) # {'y': 20, 'x': 0, 'parent': 'self.get(Fusssoldat2_194)', 'create_object': 'OverlayRedux2_443'}
                self.get(Watersplosh_444).BringToBack()
                SoundSetListenerPosition(self.get(Follower_442).x, self.get(Follower_442).y)
                SoundAutoPlayPosition('slosh'+str(randrange(4)+1)+'.wav', self.get(Fusssoldat2_194).x, self.get(Fusssoldat2_194).y)
            self.set_event_id(1507)
            if select(self.get(Fusssoldat2_194).values.get(10, 0) > 0):
                self.get(Fusssoldat2_194).values[10] -= 1
            self.set_event_id(1508)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            self.every(0.3) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat_193).x, self.get(Fusssoldat_193).y+14, 0, 0, 0))):
                SoundAutoPlay('gravel'+str(randrange(4)+1)+'.wav')
            self.set_event_id(1509)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            self.every(0.3) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat_193).x, self.get(Fusssoldat_193).y+14, 192, 192, 192))):
                SoundAutoPlay('street'+str(randrange(5)+1)+'.wav')
            self.set_event_id(1510)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            self.every(0.3) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat_193).x, self.get(Fusssoldat_193).y+14, 128, 128, 0))):
                SoundAutoPlay('wood'+str(randrange(4)+1)+'.wav')
            self.set_event_id(1511)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            self.every(0.3) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat_193).x, self.get(Fusssoldat_193).y+14, 0, 255, 0))):
                SoundAutoPlay('grass'+str(randrange(4)+1)+'.wav')
            self.set_event_id(1512)
            if (select(self.get(Strafing_219).CompareSpeed(0)) and
            self.every(0.3) and
            select(self.get(OverlayRedux2_443).OverlayMatchColorRGB(self.get(Fusssoldat_193).x, self.get(Fusssoldat_193).y+14, 0, 0, 255))):
                self.create_object(OverlayRedux2_443, self.get(Fusssoldat_193).x + 0, self.get(Fusssoldat_193).x + 20) # {'y': 20, 'x': 0, 'parent': 'self.get(Fusssoldat_193)', 'create_object': 'OverlayRedux2_443'}
                self.get(Watersplosh_444).BringToBack()
                SoundAutoPlay('slosh'+str(randrange(4)+1)+'.wav')
        pass
    
