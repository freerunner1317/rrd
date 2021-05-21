-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: pdd
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question` varchar(250) DEFAULT NULL,
  `picture_name` varchar(80) DEFAULT NULL,
  `first_answer` varchar(250) DEFAULT NULL,
  `second_answer` varchar(350) DEFAULT NULL,
  `third_answer` varchar(350) DEFAULT NULL,
  `right_answer` int DEFAULT NULL,
  `explain` varchar(500) DEFAULT NULL,
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'Где Вам разрешается остановиться при движении по автомагистрали?','uW3WVRh.jpg','Только через 500 м.','В любом месте правее линии, обозначающей край проезжей части.','В любом месте у края проезжей части.',1,'В этой ситуации вы можете остановиться только через 500 м на специальной площадке, о чем информирует знак 7.11  «Место отдыха». Остановка вне специальных площадок на автомагистралях запрещена'),(2,'Двигаясь в темное время суток вне населенного пункта с включенными фарами дальнего света, Вы догнали движущееся впереди транспортное средство. Ваши действия?','BvnAz7t.png','Оставите включенными габаритные огни, выключив фары дальнего света.','Переключите дальний свет фар на ближний.','Допускаются оба варианта действий.',2,'Поскольку дальним светом фар могут быть ослеплены не только встречные водители, но и водители, движущиеся в попутном направлении (через зеркало заднего вида), Правила предписывают вам переключать свет на ближний во всех случаях, когда возможно ослепление'),(3,'Разрешается ли Вам выполнить разворот с заездом во двор задним ходом?','PxVNZyk.jpg','Разрешается.','Разрешается, если при этом не будут созданы помехи другим участникам движения.','Запрещается.',1,'На перекрестке движение задним ходом запрещено . Однако въезды во дворы перекрестками не являются . Значит, использовать для разворота въезд во двор с заездом в него задним ходом разрешается, если не будут созданы помехи другим участникам движения.'),(4,'Кому Вы обязаны уступить дорогу при движении прямо?','a8NkuLg.jpg','Только мотоциклу.','Мотоциклу и легковому автомобилю.','Всем транспортным средствам.',3,'На этом перекрестке неравнозначных дорог (знаки 2.4  «Уступите дорогу» и 8.13  «Направление главной дороги») Вы должны уступить дорогу мотоциклу и автобусу, поскольку они движутся по главной дороге . Следует уступить дорогу и подъехавшему справа легковому автомобилю, при разъезде с которым Вы должны руководствоваться правилами проезда перекрестков равнозначных дорог'),(5,'В данной ситуации преимущество имеет:','cLxTEKZ.jpg','Легковой автомобиль, так как он движется на подъем.','Грузовой автомобиль, так как он движется на спуск.','Грузовой автомобиль, так как препятствие находится на полосе движения легкового автомобиля.',1,'Знак 1.14  «Крутой подъем» предупреждает водителя легкового автомобиля о приближении к подъему. При затрудненном встречном разъезде на данном участке дороги преимущество имеет водитель легкового автомобиля, поскольку он движется на подъём');
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-20 16:39:40
