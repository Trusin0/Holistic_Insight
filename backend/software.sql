/*
 Navicat Premium Data Transfer

 Source Server         : software
 Source Server Type    : MySQL
 Source Server Version : 80037
 Source Host           : localhost:3306
 Source Schema         : software

 Target Server Type    : MySQL
 Target Server Version : 80037
 File Encoding         : 65001

 Date: 06/06/2024 21:01:03
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for aim
-- ----------------------------
DROP TABLE IF EXISTS `aim`;
CREATE TABLE `aim`  (
  `aim_id` int NOT NULL,
  `usr_id` int NULL DEFAULT NULL,
  `average_time` float NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`aim_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `aim_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of aim
-- ----------------------------

-- ----------------------------
-- Table structure for chimpanzee
-- ----------------------------
DROP TABLE IF EXISTS `chimpanzee`;
CREATE TABLE `chimpanzee`  (
  `chi_id` int NOT NULL,
  `usr_id` int NULL DEFAULT NULL,
  `Level` int NULL DEFAULT NULL,
  `attempt_times` int NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`chi_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `chimpanzee_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of chimpanzee
-- ----------------------------

-- ----------------------------
-- Table structure for color
-- ----------------------------
DROP TABLE IF EXISTS `color`;
CREATE TABLE `color`  (
  `color_id` int NOT NULL,
  `usr_id` int NULL DEFAULT NULL,
  `Level` int NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`color_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `color_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of color
-- ----------------------------

-- ----------------------------
-- Table structure for competition
-- ----------------------------
DROP TABLE IF EXISTS `competition`;
CREATE TABLE `competition`  (
  `com_id` int NOT NULL,
  `usr1_id` int NULL DEFAULT NULL,
  `usr2_id` int NULL DEFAULT NULL,
  `Level` int NULL DEFAULT NULL,
  `winner` int NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  `game1_id` int NULL DEFAULT NULL,
  `game2_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`com_id`) USING BTREE,
  INDEX `usr1_id`(`usr1_id` ASC) USING BTREE,
  INDEX `usr2_id`(`usr2_id` ASC) USING BTREE,
  INDEX `game1_id`(`game1_id` ASC) USING BTREE,
  INDEX `game2_id`(`game2_id` ASC) USING BTREE,
  CONSTRAINT `competition_ibfk_1` FOREIGN KEY (`usr1_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `competition_ibfk_2` FOREIGN KEY (`usr2_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `competition_ibfk_3` FOREIGN KEY (`game1_id`) REFERENCES `game` (`game_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `competition_ibfk_4` FOREIGN KEY (`game2_id`) REFERENCES `game` (`game_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of competition
-- ----------------------------

-- ----------------------------
-- Table structure for friendlist
-- ----------------------------
DROP TABLE IF EXISTS `friendlist`;
CREATE TABLE `friendlist`  (
  `friendlist_id` int NOT NULL,
  `friend1_id` int NULL DEFAULT NULL,
  `friend2_id` int NULL DEFAULT NULL,
  `establish_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`friendlist_id`) USING BTREE,
  INDEX `friend1_id`(`friend1_id` ASC) USING BTREE,
  CONSTRAINT `friendlist_ibfk_1` FOREIGN KEY (`friend1_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `friendlist_ibfk_2` FOREIGN KEY (`friend1_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of friendlist
-- ----------------------------

-- ----------------------------
-- Table structure for game
-- ----------------------------
DROP TABLE IF EXISTS `game`;
CREATE TABLE `game`  (
  `game_id` int NOT NULL,
  `test_type` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `test_id` int NULL DEFAULT NULL,
  PRIMARY KEY (`game_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of game
-- ----------------------------

-- ----------------------------
-- Table structure for number
-- ----------------------------
DROP TABLE IF EXISTS `number`;
CREATE TABLE `number`  (
  `num_id` int NOT NULL,
  `usr_id` int NULL DEFAULT NULL,
  `Level` int NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`num_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `number_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of number
-- ----------------------------

-- ----------------------------
-- Table structure for react
-- ----------------------------
DROP TABLE IF EXISTS `react`;
CREATE TABLE `react`  (
  `react_id` int NOT NULL,
  `usr_id` int NULL DEFAULT NULL,
  `react_time` float NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`react_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `react_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of react
-- ----------------------------

-- ----------------------------
-- Table structure for schulte
-- ----------------------------
DROP TABLE IF EXISTS `schulte`;
CREATE TABLE `schulte`  (
  `schulte_id` int NOT NULL,
  `usr_id` int NULL DEFAULT NULL,
  `block_size` int NULL DEFAULT NULL,
  `error_times` int NULL DEFAULT NULL,
  `cost` float NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`schulte_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `schulte_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of schulte
-- ----------------------------

-- ----------------------------
-- Table structure for sight
-- ----------------------------
DROP TABLE IF EXISTS `sight`;
CREATE TABLE `sight`  (
  `sight_id` int NOT NULL,
  `usr_id` int NULL DEFAULT NULL,
  `Level` int NULL DEFAULT NULL,
  `play_time` date NULL DEFAULT NULL,
  PRIMARY KEY (`sight_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `sight_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of sight
-- ----------------------------

-- ----------------------------
-- Table structure for usr
-- ----------------------------
DROP TABLE IF EXISTS `usr`;
CREATE TABLE `usr`  (
  `usr_id` int NOT NULL,
  `pass` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `usr_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`usr_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

DROP TABLE IF EXISTS `session`;
CREATE TABLE `session` (
  `session_id` int NOT NULL,
  `usr_id` int NOT NULL,
  `session_key` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL unique,
  `expire_time` datetime NOT NULL,
  `create_time` datetime NOT NULL,
  PRIMARY KEY (`session_id`) USING BTREE,
  INDEX `usr_id`(`usr_id` ASC) USING BTREE,
  CONSTRAINT `session_ibfk_1` FOREIGN KEY (`usr_id`) REFERENCES `usr` (`usr_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of usr
-- ----------------------------

SET FOREIGN_KEY_CHECKS = 1;
