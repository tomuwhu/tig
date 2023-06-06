/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Type    : MySQL
Source Server Version : 80013
Source Host           : localhost:3306
Source Schema         : allokep

Target Server Type    : MySQL
Target Server Version : 80013
File Encoding         : 65001

Date: 06/06/2023 17:48:51
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for aerob
-- ----------------------------
DROP TABLE IF EXISTS `aerob`;
CREATE TABLE `aerob` (
  `azon` int(4) NOT NULL AUTO_INCREMENT,
  `mkod` int(2) NOT NULL,
  `nem` tinyint(4) DEFAULT NULL,
  `allkod` int(1) DEFAULT NULL,
  `letszam` int(7) DEFAULT NULL,
  PRIMARY KEY (`azon`),
  KEY `aerob_megye` (`mkod`),
  KEY `aerob_allapot` (`allkod`),
  CONSTRAINT `aerob_allapot` FOREIGN KEY (`allkod`) REFERENCES `allapot` (`kod`),
  CONSTRAINT `aerob_megye` FOREIGN KEY (`mkod`) REFERENCES `megye` (`kod`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

-- ----------------------------
-- Records of aerob
-- ----------------------------
BEGIN;
INSERT INTO `aerob` VALUES (1, 1, 0, 1, 8701);
INSERT INTO `aerob` VALUES (2, 1, 0, 2, 2881);
INSERT INTO `aerob` VALUES (3, 1, 0, 3, 2684);
INSERT INTO `aerob` VALUES (4, 1, 1, 1, 10518);
INSERT INTO `aerob` VALUES (5, 1, 1, 2, 2100);
INSERT INTO `aerob` VALUES (6, 1, 1, 3, 3186);
INSERT INTO `aerob` VALUES (7, 2, 0, 1, 5109);
INSERT INTO `aerob` VALUES (8, 2, 0, 2, 2081);
INSERT INTO `aerob` VALUES (9, 2, 0, 3, 2156);
INSERT INTO `aerob` VALUES (10, 2, 1, 1, 6073);
INSERT INTO `aerob` VALUES (11, 2, 1, 2, 1451);
INSERT INTO `aerob` VALUES (12, 2, 1, 3, 2305);
INSERT INTO `aerob` VALUES (13, 3, 0, 1, 4246);
INSERT INTO `aerob` VALUES (14, 3, 0, 2, 1573);
INSERT INTO `aerob` VALUES (15, 3, 0, 3, 1433);
INSERT INTO `aerob` VALUES (16, 3, 1, 1, 5084);
INSERT INTO `aerob` VALUES (17, 3, 1, 2, 1166);
INSERT INTO `aerob` VALUES (18, 3, 1, 3, 1577);
INSERT INTO `aerob` VALUES (19, 4, 0, 1, 5273);
INSERT INTO `aerob` VALUES (20, 4, 0, 2, 2458);
INSERT INTO `aerob` VALUES (21, 4, 0, 3, 2890);
INSERT INTO `aerob` VALUES (22, 4, 1, 1, 6513);
INSERT INTO `aerob` VALUES (23, 4, 1, 2, 1731);
INSERT INTO `aerob` VALUES (24, 4, 1, 3, 2861);
INSERT INTO `aerob` VALUES (25, 5, 0, 1, 4318);
INSERT INTO `aerob` VALUES (26, 5, 0, 2, 1820);
INSERT INTO `aerob` VALUES (27, 5, 0, 3, 1734);
INSERT INTO `aerob` VALUES (28, 5, 1, 1, 5253);
INSERT INTO `aerob` VALUES (29, 5, 1, 2, 1129);
INSERT INTO `aerob` VALUES (30, 5, 1, 3, 2028);
INSERT INTO `aerob` VALUES (31, 6, 0, 1, 4640);
INSERT INTO `aerob` VALUES (32, 6, 0, 2, 2220);
INSERT INTO `aerob` VALUES (33, 6, 0, 3, 2655);
INSERT INTO `aerob` VALUES (34, 6, 1, 1, 6037);
INSERT INTO `aerob` VALUES (35, 6, 1, 2, 1507);
INSERT INTO `aerob` VALUES (36, 6, 1, 3, 2502);
INSERT INTO `aerob` VALUES (37, 7, 0, 1, 5506);
INSERT INTO `aerob` VALUES (38, 7, 0, 2, 2407);
INSERT INTO `aerob` VALUES (39, 7, 0, 3, 2592);
INSERT INTO `aerob` VALUES (40, 7, 1, 1, 6880);
INSERT INTO `aerob` VALUES (41, 7, 1, 2, 1731);
INSERT INTO `aerob` VALUES (42, 7, 1, 3, 2808);
INSERT INTO `aerob` VALUES (43, 8, 0, 1, 3542);
INSERT INTO `aerob` VALUES (44, 8, 0, 2, 1557);
INSERT INTO `aerob` VALUES (45, 8, 0, 3, 1620);
INSERT INTO `aerob` VALUES (46, 8, 1, 1, 4438);
INSERT INTO `aerob` VALUES (47, 8, 1, 2, 1040);
INSERT INTO `aerob` VALUES (48, 8, 1, 3, 1799);
INSERT INTO `aerob` VALUES (49, 9, 0, 1, 6284);
INSERT INTO `aerob` VALUES (50, 9, 0, 2, 2664);
INSERT INTO `aerob` VALUES (51, 9, 0, 3, 3119);
INSERT INTO `aerob` VALUES (52, 9, 1, 1, 7460);
INSERT INTO `aerob` VALUES (53, 9, 1, 2, 1695);
INSERT INTO `aerob` VALUES (54, 9, 1, 3, 3751);
INSERT INTO `aerob` VALUES (55, 10, 0, 1, 28042);
INSERT INTO `aerob` VALUES (56, 10, 0, 2, 10237);
INSERT INTO `aerob` VALUES (57, 10, 0, 3, 12498);
INSERT INTO `aerob` VALUES (58, 10, 1, 1, 34544);
INSERT INTO `aerob` VALUES (59, 10, 1, 2, 7264);
INSERT INTO `aerob` VALUES (60, 10, 1, 3, 13511);
INSERT INTO `aerob` VALUES (61, 11, 0, 1, 17714);
INSERT INTO `aerob` VALUES (62, 11, 0, 2, 6958);
INSERT INTO `aerob` VALUES (63, 11, 0, 3, 6454);
INSERT INTO `aerob` VALUES (64, 11, 1, 1, 20552);
INSERT INTO `aerob` VALUES (65, 11, 1, 2, 4648);
INSERT INTO `aerob` VALUES (66, 11, 1, 3, 7350);
INSERT INTO `aerob` VALUES (67, 12, 0, 1, 8119);
INSERT INTO `aerob` VALUES (68, 12, 0, 2, 3623);
INSERT INTO `aerob` VALUES (69, 12, 0, 3, 4158);
INSERT INTO `aerob` VALUES (70, 12, 1, 1, 9499);
INSERT INTO `aerob` VALUES (71, 12, 1, 2, 2376);
INSERT INTO `aerob` VALUES (72, 12, 1, 3, 4510);
INSERT INTO `aerob` VALUES (73, 13, 0, 1, 2253);
INSERT INTO `aerob` VALUES (74, 13, 0, 2, 1429);
INSERT INTO `aerob` VALUES (75, 13, 0, 3, 1654);
INSERT INTO `aerob` VALUES (76, 13, 1, 1, 3000);
INSERT INTO `aerob` VALUES (77, 13, 1, 2, 879);
INSERT INTO `aerob` VALUES (78, 13, 1, 3, 1647);
INSERT INTO `aerob` VALUES (79, 14, 0, 1, 4522);
INSERT INTO `aerob` VALUES (80, 14, 0, 2, 2266);
INSERT INTO `aerob` VALUES (81, 14, 0, 3, 2905);
INSERT INTO `aerob` VALUES (82, 14, 1, 1, 5746);
INSERT INTO `aerob` VALUES (83, 14, 1, 2, 1563);
INSERT INTO `aerob` VALUES (84, 14, 1, 3, 3280);
INSERT INTO `aerob` VALUES (85, 15, 0, 1, 5642);
INSERT INTO `aerob` VALUES (86, 15, 0, 2, 2952);
INSERT INTO `aerob` VALUES (87, 15, 0, 3, 3441);
INSERT INTO `aerob` VALUES (88, 15, 1, 1, 7148);
INSERT INTO `aerob` VALUES (89, 15, 1, 2, 2004);
INSERT INTO `aerob` VALUES (90, 15, 1, 3, 3599);
INSERT INTO `aerob` VALUES (91, 16, 0, 1, 6596);
INSERT INTO `aerob` VALUES (92, 16, 0, 2, 2847);
INSERT INTO `aerob` VALUES (93, 16, 0, 3, 2973);
INSERT INTO `aerob` VALUES (94, 16, 1, 1, 8508);
INSERT INTO `aerob` VALUES (95, 16, 1, 2, 1961);
INSERT INTO `aerob` VALUES (96, 16, 1, 3, 3402);
INSERT INTO `aerob` VALUES (97, 17, 0, 1, 5099);
INSERT INTO `aerob` VALUES (98, 17, 0, 2, 2623);
INSERT INTO `aerob` VALUES (99, 17, 0, 3, 2744);
INSERT INTO `aerob` VALUES (100, 17, 1, 1, 6501);
INSERT INTO `aerob` VALUES (101, 17, 1, 2, 1695);
INSERT INTO `aerob` VALUES (102, 17, 1, 3, 3020);
INSERT INTO `aerob` VALUES (103, 18, 0, 1, 9160);
INSERT INTO `aerob` VALUES (104, 18, 0, 2, 4484);
INSERT INTO `aerob` VALUES (105, 18, 0, 3, 4739);
INSERT INTO `aerob` VALUES (106, 18, 1, 1, 11295);
INSERT INTO `aerob` VALUES (107, 18, 1, 2, 2990);
INSERT INTO `aerob` VALUES (108, 18, 1, 3, 4971);
INSERT INTO `aerob` VALUES (109, 19, 0, 1, 8470);
INSERT INTO `aerob` VALUES (110, 19, 0, 2, 5206);
INSERT INTO `aerob` VALUES (111, 19, 0, 3, 5446);
INSERT INTO `aerob` VALUES (112, 19, 1, 1, 11492);
INSERT INTO `aerob` VALUES (113, 19, 1, 2, 3203);
INSERT INTO `aerob` VALUES (114, 19, 1, 3, 5303);
INSERT INTO `aerob` VALUES (115, 20, 0, 1, 9148);
INSERT INTO `aerob` VALUES (116, 20, 0, 2, 5459);
INSERT INTO `aerob` VALUES (117, 20, 0, 3, 6734);
INSERT INTO `aerob` VALUES (118, 20, 1, 1, 12669);
INSERT INTO `aerob` VALUES (119, 20, 1, 2, 3478);
INSERT INTO `aerob` VALUES (120, 20, 1, 3, 6722);
COMMIT;

-- ----------------------------
-- Table structure for allapot
-- ----------------------------
DROP TABLE IF EXISTS `allapot`;
CREATE TABLE `allapot` (
  `kod` int(1) NOT NULL,
  `nev` varchar(30) COLLATE utf8mb4_hungarian_ci DEFAULT NULL,
  PRIMARY KEY (`kod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

-- ----------------------------
-- Records of allapot
-- ----------------------------
BEGIN;
INSERT INTO `allapot` VALUES (1, 'egészséges');
INSERT INTO `allapot` VALUES (2, 'fejlesztést igényel');
INSERT INTO `allapot` VALUES (3, 'fokozott fejlesztést igényel');
COMMIT;

-- ----------------------------
-- Table structure for megye
-- ----------------------------
DROP TABLE IF EXISTS `megye`;
CREATE TABLE `megye` (
  `kod` int(2) NOT NULL,
  `nev` varchar(30) COLLATE utf8mb4_hungarian_ci DEFAULT NULL,
  `letszam` int(7) DEFAULT NULL,
  PRIMARY KEY (`kod`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

-- ----------------------------
-- Records of megye
-- ----------------------------
BEGIN;
INSERT INTO `megye` VALUES (1, 'Győr-Moson-Sopron', 56762);
INSERT INTO `megye` VALUES (2, 'Komárom-Esztergom', 34932);
INSERT INTO `megye` VALUES (3, 'Vas', 28640);
INSERT INTO `megye` VALUES (4, 'Veszprém', 39670);
INSERT INTO `megye` VALUES (5, 'Zala', 30155);
INSERT INTO `megye` VALUES (6, 'Somogy', 35028);
INSERT INTO `megye` VALUES (7, 'Baranya', 41661);
INSERT INTO `megye` VALUES (8, 'Tolna', 25582);
INSERT INTO `megye` VALUES (9, 'Fejér', 48895);
INSERT INTO `megye` VALUES (10, 'Budapest', 220520);
INSERT INTO `megye` VALUES (11, 'Pest', 133556);
INSERT INTO `megye` VALUES (12, 'Bács-Kiskun', 60865);
INSERT INTO `megye` VALUES (13, 'Nógrád', 20692);
INSERT INTO `megye` VALUES (14, 'Heves', 37746);
INSERT INTO `megye` VALUES (15, 'Jász-Nagykun-Szolnok', 46511);
INSERT INTO `megye` VALUES (16, 'Csongrád-Csanád', 48522);
INSERT INTO `megye` VALUES (17, 'Békés', 39919);
INSERT INTO `megye` VALUES (18, 'Hajdú-Bihar', 67853);
INSERT INTO `megye` VALUES (19, 'Szabolcs-Szatmár-Bereg', 73108);
INSERT INTO `megye` VALUES (20, 'Borsod-Abaúj-Zemplén', 85505);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
