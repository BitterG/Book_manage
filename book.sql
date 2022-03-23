/*
 Navicat MySQL Data Transfer

 Source Server         : abc
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : book

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 23/03/2022 19:35:44
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for borrow
-- ----------------------------
DROP TABLE IF EXISTS `borrow`;
CREATE TABLE `borrow`  (
  `Book_id` int UNSIGNED NOT NULL,
  `Book_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `User_id` int UNSIGNED NOT NULL,
  `User_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Borrow_date` datetime NOT NULL,
  `User_phone` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Borrow_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`Borrow_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of borrow
-- ----------------------------
INSERT INTO `borrow` VALUES (6, '狂人日记', 1, '用户一', '2022-03-19 15:04:50', '12345678901', 2);

-- ----------------------------
-- Table structure for map
-- ----------------------------
DROP TABLE IF EXISTS `map`;
CREATE TABLE `map`  (
  `Book_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `Book_name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Book_cate` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Book_author` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Book_quantity` int UNSIGNED NOT NULL,
  `is_show` bit(1) NOT NULL DEFAULT b'1',
  `is_saleoff` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`Book_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of map
-- ----------------------------
INSERT INTO `map` VALUES (1, '毛主席语录', '政治哲学', '毛泽东', 3399, b'1', b'0');
INSERT INTO `map` VALUES (2, '圣经', '宗教经典', '合集', 4999, b'1', b'0');
INSERT INTO `map` VALUES (3, '小王子', '小说', '安托万·德·圣·埃克苏佩里', 8499, b'1', b'0');
INSERT INTO `map` VALUES (4, '安徒生童话', '童话集', '安徒生', 2799, b'1', b'0');
INSERT INTO `map` VALUES (5, '共产党宣言', '政治哲学', '合集', 4880, b'1', b'0');
INSERT INTO `map` VALUES (6, '狂人日记', '小说', '周树人', 4299, b'1', b'0');
INSERT INTO `map` VALUES (7, '红楼梦', '小说', '曹雪芹', 7999, b'1', b'0');
INSERT INTO `map` VALUES (8, '童年', '小说', '高尔基', 1998, b'1', b'0');
INSERT INTO `map` VALUES (9, '格列佛游记', '小说', '乔纳森·斯威夫特', 3388, b'1', b'0');
INSERT INTO `map` VALUES (10, '钢铁是怎样炼成的', '小说', '保尔·柯察金', 2788, b'1', b'0');
INSERT INTO `map` VALUES (11, '战争与和平', '小说', '列夫·托尔斯泰', 3499, b'1', b'0');
INSERT INTO `map` VALUES (12, '呼啸山庄', '小说', '艾米莉·勃朗特', 2899, b'1', b'0');
INSERT INTO `map` VALUES (13, '雨后小故事', '漫画', '析木兮', 2899, b'1', b'0');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `User_id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `User_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `User_date` date NOT NULL,
  `User_phone` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `User_address` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `User_password` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`User_id`, `User_phone`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 13 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '用户一', '2022-03-15', '12345678901', '本星际云＞太阳系＞地月系＞地球', '12345678');
INSERT INTO `user` VALUES (2, '苦瓜', '2022-03-15', '12345678901', '本星际云＞太阳系＞地月系＞地球', '123123123');
INSERT INTO `user` VALUES (3, '我是用户', '2022-03-15', '123456', '详细的地址', '321321321');
INSERT INTO `user` VALUES (4, '测试账号', '2022-03-18', '13488888888', '这是一个地址', '12345678912');
INSERT INTO `user` VALUES (6, '测2试账号', '2022-03-18', '13488888888', '这是一个地址', '12345678912');
INSERT INTO `user` VALUES (10, '测试用户1', '2022-03-18', '12388888888', '地址123', '123456');
INSERT INTO `user` VALUES (11, '一个u', '2022-03-18', '1234567', '地址啊', '21284');
INSERT INTO `user` VALUES (12, '测试用户3', '2022-03-18', '2211233', '地址345', '123789');
INSERT INTO `user` VALUES (13, '我是个傻逼', '2022-03-18', '10086', '地址', '000000');

SET FOREIGN_KEY_CHECKS = 1;
