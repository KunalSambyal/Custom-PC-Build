-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: components
-- ------------------------------------------------------
-- Server version	5.5.62

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

CREATE DATABASE IF NOT EXISTS components;
USE components;

--
-- Table structure for table `cpus`
--

DROP TABLE IF EXISTS `cpus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cpus` (
  `Name` varchar(30) DEFAULT NULL,
  `Core` int(11) DEFAULT NULL,
  `THREAD` int(11) DEFAULT NULL,
  `Speed` varchar(20) DEFAULT NULL,
  `Socket` varchar(30) DEFAULT NULL,
  `Model` varchar(10) NOT NULL DEFAULT '',
  `wattage` int(11) DEFAULT NULL,
  `Price` decimal(12,2) DEFAULT '0.00',
  PRIMARY KEY (`Model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpus`
--

LOCK TABLES `cpus` WRITE;
/*!40000 ALTER TABLE `cpus` DISABLE KEYS */;
INSERT INTO `cpus` VALUES ('Ryzen 5 3600X',6,12,'3.8 - 4.4 Ghz','AM4','AMD-350',95,22000.00),('Ryzen 7 3700X',8,16,'3.6 - 4.4 Ghz','AM4','AMD-370',65,24000.00),('Ryzen 7 3800X',8,16,'3.8 - 4.7 Ghz','AM4','AMD-371',105,30000.00),('Ryzen 9 3900',12,24,'3.1 - 4.3 Ghz','AM4','AMD-390',65,37000.00),('Ryzen 9 3900X',12,24,'3.8 - 4.6 Ghz','AM4','AMD-391',105,40000.00),('Ryzen 5 5500',6,12,'3.6 - 4.2 Ghz','AM4','AMD-550',65,11000.00),('Ryzen 5 5500G',6,12,'3.9 - 4.4 Ghz','AM4','AMD-551',65,20000.00),('Ryzen 5 5600X',6,12,'3.7 - 4.4 Ghz','AM4','AMD-552',65,22500.00),('Ryzen 7 5700',8,16,'3.7 - 4.6 Ghz','AM4','AMD-570',65,24000.00),('Ryzen 7 5700X',8,16,'3.4 - 4.6 Ghz','AM4','AMD-571',65,27000.00),('Ryzen 7 5800',8,16,'3.4 - 4.6 Ghz','AM4','AMD-572',65,18000.00),('Ryzen 7 5800X',8,16,'3.8 - 4.7 Ghz','AM4','AMD-573',105,21000.00),('Ryzen 9 5900',12,24,'3.0 - 4.7 Ghz','AM4','AMD-590',65,28000.00),('Ryzen 9 5900X',12,24,'3.7 - 4.8 Ghz','AM4','AMD-591',105,32000.00),('Ryzen 9 5950X',16,32,'3.4 - 4.9 Ghz','AM4','AMD-592',105,38000.00),('Ryzen 5 7600',6,12,'3.8 - 5.1 Ghz','AM5','AMD-750',65,18500.00),('Ryzen 5 7600X',6,12,'4.7 - 5.3 Ghz','AM5','AMD-751',105,19500.00),('Ryzen 5 7600X3D',6,12,'4.1 - 4.7 Ghz','AM5','AMD-752',65,31000.00),('Ryzen 7 7700',8,16,'3.8 - 5.3 Ghz','AM5','AMD-770',65,29000.00),('Ryzen 7 7700X',8,16,'4.5 - 5.4 Ghz','AM5','AMD-771',105,33000.00),('Ryzen 7 7700X3D',8,16,'4.2 - 5.0 Ghz','AM5','AMD-772',120,41000.00),('Ryzen 9 7900',12,24,'3.7 - 5.4 Ghz','AM5','AMD-790',65,35000.00),('Ryzen 9 7900X',12,24,'4.7 - 5.6 Ghz','AM5','AMD-791',170,37000.00),('Ryzen 9 7950X',16,32,'4.5 - 5.7 Ghz','AM5','AMD-792',170,48000.00),('Ryzen 5 8400F',6,12,'4.2 - 4.7 Ghz','AM5','AMD-850',65,15400.00),('Ryzen 5 8500G',6,12,'3.5 - 5.0 Ghz','AM5','AMD-851',65,13800.00),('Ryzen 5 8600G',6,12,'4.3 - 5.0 Ghz','AM5','AMD-852',65,17000.00),('Ryzen 7 8700G',8,16,'4.2 - 5.1 Ghz','AM5','AMD-870',65,32000.00),('Ryzen 5 9600X',6,12,'3.9 - 5.4 Ghz','AM5','AMD-950',65,25000.00),('Ryzen 7 9700X',8,16,'3.8 - 5.5 Ghz','AM5','AMD-970',65,32000.00),('Ryzen 7 9700X3D',8,16,'4.7 - 5.2 Ghz','AM5','AMD-971',120,30000.00),('Ryzen 9 9900X',12,24,'4.4 - 5.6 Ghz','AM5','AMD-990',120,42000.00),('Ryzen 9 9950X',16,32,'4.3 - 5.7 Ghz','AM5','AMD-991',170,56000.00),('Core i5 10400',6,12,'2.9 - 4.3 Ghz','Socket 1200','INT-500',65,10500.00),('Core i5 10400F',6,12,'2.9 - 4.3 Ghz','Socket 1200','INT-501',65,9200.00),('Core i5 10500',6,12,'3.1 - 4.5 Ghz','Socket 1200','INT-502',65,12000.00),('Core i5 10600',6,12,'3.3 - 4.8 Ghz','Socket 1200','INT-503',65,16000.00),('Core i5 10600K',6,12,'4.1 - 4.8 Ghz','Socket 1200','INT-504',125,21000.00),('Core i5 10600KF',6,12,'4.1 - 4.8 Ghz','Socket 1200','INT-505',95,19000.00),('Core i5 11400',6,12,'2.6 - 4.4 Ghz','Socket 1200','INT-510',65,8500.00),('Core i5 11400F',6,12,'2.6 - 4.4 Ghz','Socket 1200','INT-511',65,10500.00),('Core i5 11500',6,12,'2.7 - 4.6 Ghz','Socket 1200','INT-512',65,13000.00),('Core i5 11600',6,12,'2.8 - 4.8 Ghz','Socket 1200','INT-513',65,15000.00),('Core i5 11600K',6,12,'3.9 - 4.9 Ghz','Socket 1200','INT-514',125,17500.00),('Core i5 11600KF',6,12,'3.9 - 4.9 Ghz','Socket 1200','INT-515',125,21000.00),('Core i5 12400',6,12,'2.5 - 4.4 Ghz','Socket 1700','INT-520',65,11000.00),('Core i5 12400F',6,12,'2.5 - 4.4 Ghz','Socket 1700','INT-521',65,13000.00),('Core i5 12500',6,12,'3.0 - 4.6 Ghz','Socket 1700','INT-522',65,17000.00),('Core i5 12600',6,12,'3.3 - 4.8 Ghz','Socket 1700','INT-523',65,17000.00),('Core i5 12600K',10,16,'3.7 - 4.9 Ghz','Socket 1700','INT-524',125,18500.00),('Core i5 12600KF',10,16,'3.7 - 4.9 Ghz','Socket 1700','INT-525',125,20000.00),('Core i5 13500',14,20,'2.5 - 4.8 Ghz','Socket 1700','INT-532',65,21500.00),('Core i5 13600',14,20,'2.7 - 5.0 Ghz','Socket 1700','INT-533',65,25000.00),('Core i5 13600K',14,20,'3.5 - 5.1 Ghz','Socket 1700','INT-534',125,28000.00),('Core i5 13600KF',14,20,'3.5 - 5.1 Ghz','Socket 1700','INT-535',125,30000.00),('Core i5 14400F',10,16,'2.5 - 4.7 Ghz','Socket 1700','INT-540',65,24000.00),('Core i5 14400T',10,16,'1.5 - 4.5 Ghz','Socket 1700','INT-541',35,30000.00),('Core i5 14600',14,20,'2.7 - 5.2 Ghz','Socket 1700','INT-543',65,20000.00),('Core i5 14600K',14,20,'3.5 - 5.3 Ghz','Socket 1700','INT-544',125,23000.00),('Core i5 14600KF',14,20,'3.5 - 5.3 Ghz','Socket 1700','INT-545',125,25900.00),('Core i7 10700',8,16,'2.9 - 4.8 Ghz','Socket 1200','INT-700',65,24500.00),('Core i7 10700F',8,16,'2.9 - 4.8 Ghz','Socket 1200','INT-701',65,25000.00),('Core i7 10700K',8,16,'3.8 - 5.1 Ghz','Socket 1200','INT-702',125,28500.00),('Core i7 10700KF',8,16,'3.8 - 5.1 Ghz','Socket 1200','INT-703',125,33000.00),('Core i7 11700T',8,16,'1.4 - 4.6 Ghz','Socket 1200','INT-710',35,28000.00),('Core i7 11700',8,16,'2.5 - 4.9 Ghz','Socket 1200','INT-711',65,22500.00),('Core i7 11700F',8,16,'2.5 - 4.9 Ghz','Socket 1200','INT-712',65,24000.00),('Core i7 11700K',8,16,'3.6 - 5.0 Ghz','Socket 1200','INT-713',125,31000.00),('Core i7 11700KF',8,16,'3.6 - 5.0 Ghz','Socket 1200','INT-714',125,36000.00),('Core i7 12700T',12,20,'1.4 - 4.7 Ghz','Socket 1700','INT-720',35,27500.00),('Core i7 12700E',12,20,'2.1 - 4.8 Ghz','Socket 1700','INT-721',65,30000.00),('Core i7 12700',12,20,'2.1 - 4.9 Ghz','Socket 1700','INT-722',65,26000.00),('Core i7 12700F',12,20,'2.1 - 4.9 Ghz','Socket 1700','INT-723',65,28500.00),('Core i7 12700K',12,20,'3.6 - 5.0 Ghz','Socket 1700','INT-724',125,30000.00),('Core i7 12700KF',12,20,'3.6 - 5.0 Ghz','Socket 1700','INT-725',125,31500.00),('Core i7 13700TE',16,24,'1.1 - 4.8 Ghz','Socket 1700','INT-730',35,34000.00),('Core i7 13700T',16,24,'1.4 - 4.9 Ghz','Socket 1700','INT-731',35,36000.00),('Core i7 13700E',16,24,'1.9 - 5.1 Ghz','Socket 1700','INT-732',65,35500.00),('Core i7 13700',16,24,'2.1 - 5.2 Ghz','Socket 1700','INT-733',65,34000.00),('Core i7 13700F',16,24,'2.1 - 5.2 Ghz','Socket 1700','INT-734',65,35000.00),('Core i7 13700K',16,24,'3.4 - 5.4 Ghz','Socket 1700','INT-735',125,40000.00),('Core i7 13700KF',16,24,'3.4 - 5.4 Ghz','Socket 1700','INT-736',125,42000.00),('Core i7 14701E',8,16,'2.6 - 5.4 Ghz','Socket 1700','INT-740',65,28000.00),('Core i7 14700T',20,28,'1.3 - 5.2 Ghz','Socket 1700','INT-741',35,43000.00),('Core i7 14700',20,28,'2.1 - 5.4 Ghz','Socket 1700','INT-742',65,30000.00),('Core i7 14700F',20,28,'2.1 - 5.4 Ghz','Socket 1700','INT-743',65,31200.00),('Core i7 14700K',20,28,'3.4 - 5.6 Ghz','Socket 1700','INT-744',125,39000.00),('Core i7 14700KF',20,28,'3.4 - 5.6 Ghz','Socket 1700','INT-745',125,45000.00),('Core i7 9700',8,8,'3.0 - 4.7 Ghz','Socket 1151','INT-790',65,16000.00),('Core i7 9700F',8,8,'3.0 - 4.7 Ghz','Socket 1151','INT-791',65,19000.00),('Core i7 9700K',8,8,'3.6 - 4.9 Ghz','Socket 1151','INT-792',95,20000.00),('Core i7 9700KF',8,8,'3.6 - 4.9 Ghz','Socket 1151','INT-793',95,24000.00),('Core i7 9800X',8,16,'3.8 - 4.5 Ghz','Socket 2066','INT-798',165,48000.00),('Core i9 10800F',10,20,'2.7 - 5.0 Ghz','Socket 1200','INT-900',65,25000.00),('Core i9 10900',10,20,'2.8 - 5.2 Ghz','Socket 1200','INT-901',65,35000.00),('Core i9 10900F',10,20,'2.8 - 5.2 Ghz','Socket 1200','INT-902',65,37500.00),('Core i9 10900K',10,20,'3.7 - 5.3 Ghz','Socket 1200','INT-903',125,45000.00),('Core i9 10900KF',10,20,'3.7 - 5.3 Ghz','Socket 1200','INT-904',125,48000.00),('Core i9 10900X',10,20,'3.7 - 4.7 Ghz','Socket 2066','INT-905',165,62000.00),('Core i9 11900T',8,16,'1.5 - 4.9 Ghz','SOcket 1200','INT-910',35,34000.00),('Core i9 11900F',8,16,'2.5 - 5.2 Ghz','Socket 1200','INT-911',65,37500.00),('Core i9 11900',8,16,'2.5 - 5.2 Ghz','Socket 1200','INT-912',65,40000.00),('Core i9 11900KF',8,16,'3.5 - 5.3 Ghz','Socket 1200','INT-913',125,45000.00),('Core i9 11900K',8,16,'3.5 - 5.3 Ghz','Socket 1200','INT-914',125,48000.00),('Core i9 12900T',16,24,'1.4 - 4.9 Ghz','Socket 1700','INT-920',35,42000.00),('Core i9 12900',16,24,'2.4 - 5.1 Ghz','Socket 1700','INT-921',65,46000.00),('Core i9 12900F',16,24,'2.4 - 5.1 Ghz','Socket 1700','INT-922',65,47500.00),('Core i9 12900K',16,24,'3.2 - 5.2 Ghz','Socket 1700','INT-923',125,55000.00),('Core i9 12900KF',16,24,'3.2 - 5.2 Ghz','Socket 1700','INT-924',125,57500.00),('Core i9 12900KS',16,24,'3.4 - 5.5 Ghz','Socket 1700','INT-925',150,60000.00),('Core i9 13900TE',24,32,'1.0 - 5.0 Ghz','Socket 1700','INT-930',35,42000.00),('Core i9 13900T',24,32,'1.1 - 5.3 Ghz','Socket 1700','INT-931',35,43500.00),('Core i9 13900E',24,32,'1.8 - 5.2 Ghz','Socket 1700','INT-932',65,41000.00),('Core i9 13900',24,32,'2.0 - 5.6 Ghz','Socket 1700','INT-933',65,51000.00),('Core i9 13900F',24,32,'2.0 - 5.6 GHz','Socket 1700','INT-934',65,49000.00),('Core i9 13900K',24,32,'3.0 - 5.8 Ghz','Socket 1700','INT-935',125,53000.00),('Core i9 13900KF',24,32,'3.0 - 5.8 Ghz','Socket 1700','INT-936',125,54500.00),('Core i9 13900KS',24,32,'3.2 - 6.0 Ghz','Socket 1700','INT-937',125,55000.00),('Core i9 14901TE',8,16,'2.3 - 5.5 Ghz','Socket 1700','INT-940',45,44500.00),('Core i9 14901E',8,16,'2.8 - 5.6 Ghz','Socket 1700','INT-941',65,44000.00),('Core i9 14901KE',8,16,'3.8 - 5.8 Ghz','Socket 1700','INT-942',125,60000.00),('Core i9 14900T',24,32,'1.1 - 5.5 Ghz','Socket 1700','INT-943',35,48000.00),('Core i9 14900',24,32,'2.0 - 5.8 Ghz','Socket 1700','INT-944',65,53000.00),('Core i9 14900F',24,32,'2.0 - 5.8 Ghz','Socket 1700','INT-945',65,55300.00),('Core i9 14900K',24,32,'3.2 - 6.0 Ghz','Socket 1700','INT-946',125,58000.00),('Core i9 14900KF',24,32,'3.2 - 6.0 Ghz','Socket 1700','INT-947',125,58500.00),('Core i9 14900KS',24,32,'3.2 - 6.2 Ghz','Socket 1700','INT-948',125,65000.00),('Core i9 9900',8,16,'3.1 - 5.0 Ghz','Socket 1151','INT-990',65,30000.00),('Core i9 9900K',8,16,'3.6 - 5.0 Ghz','Socket 1151','INT-991',95,35000.00),('Core i9 9900KS',8,16,'4.0 - 5.0 Ghz','Socket 1151','INT-992',127,42000.00);
/*!40000 ALTER TABLE `cpus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gpus`
--

DROP TABLE IF EXISTS `gpus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gpus` (
  `Name` varchar(25) NOT NULL,
  `Memory` varchar(20) NOT NULL,
  `ClockSpeed` varchar(10) NOT NULL,
  `Model` varchar(10) NOT NULL,
  `Prefix` varchar(20) DEFAULT NULL,
  `Wattage` int(11) DEFAULT NULL,
  `Price` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`Model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gpus`
--

LOCK TABLES `gpus` WRITE;
/*!40000 ALTER TABLE `gpus` DISABLE KEYS */;
INSERT INTO `gpus` VALUES ('Gtx 1050','3Gb Gddr5','1.75Ghz','GTX-100','GeForce',75,12000.00),('Gtx 1050 Ti','4Gb Gddr5','1.75Ghz','GTX-101','GeForce',75,15000.00),('Gtx 1060','6Gb Gddr5','2Ghz','GTX-102','GeForce',120,18000.00),('Gtx 1060','8Gb Gddr5x','1Ghz','GTX-103','GeForce',120,19000.00),('Gtx 1070','8Gb Gddr5','1Ghz','GTX-104','GeForce',150,10000.00),('Gtx 1070 Ti','8Gb Gddr5','2Ghz','GTX-105','GeForce',180,15000.00),('Gtx 1080','8Gb Gddr5x','1.25Ghz','GTX-106','GeForce',180,16500.00),('Gtx 1080 Ti','12Gb Gddr5x','1.37Ghz','GTX-107','GeForce',250,18000.00),('Gtx 1630','4Gb Gddr5','1.5Ghz','GTX-160','GeForce',75,16500.00),('Gtx 1650','4Gb Gddr5','2Ghz','GTX-161','GeForce',75,17500.00),('Gtx 1650 Super','4Gb Gddr6','1.5Ghz','GTX-162','GeForce',100,18700.00),('Gtx 1660','6Gb Gddr5','2Ghz','GTX-163','GeForce',120,20000.00),('Gtx 1660 Ti','6Gb Gddr6','1.5Ghz','GTX-164','GeForce',120,22000.00),('Gtx 1660 Super','6Gb Gddr6','1.75Ghz','GTX-165','GeForce',125,24000.00),('Rtx 2060','6Gb Gddr6','1.75Ghz','RTX-200','GeForce',160,28000.00),('Rtx 2060','12Gb Gddr6','1.75Ghz','RTX-201','GeForce',160,32000.00),('Rtx 2060 Super','8Gb Gddr6','1.75Ghz','RTX-202','GeForce',175,30000.00),('Rtx 2070','8Gb Gddr6','1.75Ghz','RTX-203','GeForce',175,30000.00),('Rtx 2070 Super','8Gb Gddr6','1.75Ghz','RTX-204','GeForce',215,39000.00),('Rtx 2080','8Gb Gddr6','1.75Ghz','RTX-205','GeForce',215,35000.00),('Rtx 2080 Super','8Gb Gddr6','1.9Ghz','RTX-206','GeForce',250,110000.00),('Rtx 2080 Ti','12Gb Gddr6','2Ghz','RTX-207','GeForce',250,62000.00),('Rtx 3050','4Gb Gddr6','1.5Ghz','RTX-300','GeForce',70,19000.00),('Rtx 3050','6Gb Gddr6','1.75Ghz','RTX-301','GeForce',70,17000.00),('Rtx 3050','8Gb Gddr6','1.75Ghz','RTX-302','GeForce',130,22000.00),('Rtx 3060','8Gb Gddr6','1.87Ghz','RTX-303','GeForce',170,24500.00),('Rtx 3060 Ti','8Gb Gddr6x','1.18Ghz','RTX-304','GeForce',200,28000.00),('Rtx 3060','12Gb Gddr6','1.32Ghz','RTX-305','GeForce',170,30000.00),('Rtx 3070','8Gb Gddr6','1.5Ghz','RTX-306','GeForce',220,45000.00),('Rtx 3070 Ti','8Gb Gddr6x','1.57Ghz','RTX-307','GeForce',290,48000.00),('Rtx 3070 Ti','16Gb Gddr6x','1.57Ghz','RTX-308','GeForce',290,52000.00),('Rtx 3080','10Gb Gddr6x','1.44Ghz','RTX-309','GeForce',320,48000.00),('Rtx 3080','12Gb Gddr6x','1.26Ghz','RTX-310','GeForce',320,50000.00),('Rtx 3080 Ti','20Gb Gddr6x','1.33Ghz','RTX-311','GeForce',320,57000.00),('Rtx 3090','24Gb Gddr6x','1.4Ghz','RTX-312','GeForce',350,68000.00),('Rtx 3090 Ti','24Gb Gddr6x','1.56Ghz','RTX-313','GeForce',350,90000.00),('Rtx 4050','6Gb Gddr6','2.25Ghz','RTX-400','GeForce',115,22000.00),('Rtx 4060','8Gb Gddr6','2.12Ghz','RTX-401','GeForce',115,26000.00),('Rtx 4060 Ti','8Gb Gddr6','2.25Ghz','RTX-402','GeForce',165,35000.00),('Rtx 4060 Ti','16Gb Gddr6','2.25Ghz','RTX-403','GeForce',165,38000.00),('Rtx 4070','12Gb Gddr6x','1.3Ghz','RTX-404','GeForce',200,44000.00),('Rtx 4070 Super','12Gb Gddr6x','1.3Ghz','RTX-405','GeForce',220,48000.00),('Rtx 4070 Ti','12Gb Gddr6x','2.31Ghz','RTX-406','GeForce',285,50000.00),('Rtx 4070 Ti Super','16Gb Gddr6x','2.34Ghz','RTX-407','GeForce',285,51000.00),('Rtx 4080','12Gb Gddr6x','2.31Ghz','RTX-408','GeForce',320,55000.00),('Rtx 4080','16Gb Gddr6x','2.2Ghz','RTX-409','GeForce',320,60000.00),('Rtx 4080 Super','16Gb Gddr6x','2.3Ghz','RTX-410','GeForce',320,65000.00),('Rtx 4080 Ti','16Gb Gddr6x','2.34Ghz','RTX-412','GeForce',400,68000.00),('Rtx 4090','24Gb Gddr6x','2.23Ghz','RTX-413','GeForce',450,90000.00),('Rtx 4090 Ti','24Gb Gddr6x','2.32Ghz','RTX-414','GeForce',600,120000.00),('RTX Titan','24Gb','1.77Ghz','RTX-999','GeForce',350,155000.00),('Rx 5300 Xt','4Gb Gddr5','1.75Ghz','RX-500','Radeon',100,12000.00),('Rx 5500','4Gb Gddr6','1.75Ghz','RX-501','Radeon',130,14500.00),('Rx 5500 Xt','4Gb Gddr6','1.75Ghz','RX-502','Radeon',130,16000.00),('Rx 5600','6Gb Gddr6','1.5Ghz','RX-503','Radeon',150,17000.00),('Rx 5700','8Gb Gddr6','1.75Ghz','RX-504','Radeon',180,18000.00),('Rx 5700 Xt','8Gb Gddr6','1.75Ghz','RX-505','Radeon',225,20000.00),('Rx 6500 Xt','4Gb Gddr6','2.2Ghz','RX-600','Radeon',107,18500.00),('Rx 6600','8Gb Gddr6','1.75Ghz','RX-601','Radeon',132,24000.00),('Rx 6600 Xt','8Gb Gddr6','2Ghz','RX-602','Radeon',160,29000.00),('Rx 6700','10Gb Gddr6','2Ghz','RX-603','Radeon',180,38000.00),('Rx 6700 Xt','12Gb Gddr6','2Ghz','RX-604','Radeon',220,42000.00),('Rx 6800','16Gb Gddr6','2Ghz','RX-605','Radeon',200,45000.00),('Rx 6800 Xt','16Gb Gddr6','2Ghz','RX-606','Radeon',300,52000.00),('Rx 6900 Xt','16Gb Gddr6','2Ghz','RX-607','Radeon',300,78000.00),('Rx 6950 Xt','16Gb Gddr6','2.25Ghz','RX-608','Radeon',305,85000.00),('Rx 7500 Xt','6Gb Gddr6','2.25Ghz','RX-700','Radeon',100,17500.00),('Rx 7900','8Gb Gddr6','2.25Ghz','RX-701','Radeon',165,26000.00),('Rx 7600 Xt','16Gb Gddr6','2.25Ghz','RX-702','Radeon',190,35000.00),('Rx 7700','12Gb Gddr6','2.25Ghz','RX-703','Radeon',180,40000.00),('Rx 7700 Xt','12Gb Gddr6','2.25Ghz','RX-704','Radeon',200,44000.00),('Rx 7800 Xt','16Gb Gddr6','2.4Ghz','RX-705','Radeon',300,57000.00),('Rx 7900 Xt','20Gb Gddr6','2.5Ghz','RX-706','Radeon',315,80000.00),('Rx 7950 Xt','20Gb Gddr6','2.5Ghz','RX-707','Radeon',300,82000.00),('Rx 7950 Xtx','24Gb Gddr6','2.5Ghz','RX-708','Radeon',355,85000.00),('Rx 7990 Xtx','24Gb Gddr6','3Ghz','RX-709','Radeon',405,95000.00);
/*!40000 ALTER TABLE `gpus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `memory`
--

DROP TABLE IF EXISTS `memory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `memory` (
  `Name` varchar(50) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Speed` varchar(20) DEFAULT NULL,
  `Capacity` varchar(20) DEFAULT NULL,
  `Model` varchar(20) NOT NULL DEFAULT '',
  `Price` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`Model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `memory`
--

LOCK TABLES `memory` WRITE;
/*!40000 ALTER TABLE `memory` DISABLE KEYS */;
INSERT INTO `memory` VALUES ('Corsair Vengeance LPX','ddr4','3200Mhz','8Gb','MEM-430',1900.00),('Corsair Vengeance LPX','ddr4','3200Mhz','16Gb','MEM-431',3200.00),('Adata XPG Gammix','ddr4','3200Mhz','8Gb','MEM-432',1500.00),('Adata XPG Gammix','ddr4','3200Mhz','16Gb','MEM-433',2500.00),('G.Skill Ripjaws V','ddr4','3200Mhz','8Gb','MEM-434',1500.00),('G.Skill Ripjaws V','ddr4','3200Mhz','16Gb','MEM-435',1500.00),('Adata XPG','ddr5','4800Mhz','8Gb','MEM-540',3500.00),('Corsair Vengeance','ddr5','5200Mhz','16Gb','MEM-550',4300.00),('Corsair Vengeance','ddr5','5200Mhz','16Gb','MEM-551',8500.00),('Adata XPG Lancer RGB','ddr5','5200Mhz','16Gb','MEM-552',4200.00),('G.Skill Ripjaws S5','ddr5','5200Mhz','16Gb','MEM-553',4000.00),('Adata XPG Lancer RGB','ddr5','6000Mhz','16Gb','MEM-560',5500.00),('Adata XPG Lancer RGB','ddr5','6000Mhz','32Gb','MEM-561',9000.00),('G.Skill Ripjaws S5','ddr5','6000Mhz','16Gb','MEM-562',4500.00),('G.Skill Trident Z5','ddr5','6000Mhz','16Gb','MEM-563',5000.00),('G.Skill Trident Z5 RGB','ddr5','6000Mhz','32Gb','MEM-564',10000.00),('Acer Predator Pallas II','ddr5','6000Mhz','16Gb','MEM-565',5000.00),('Acer Predator Vesta II','ddr5','6000Mhz','16Gb','MEM-566',6200.00);
/*!40000 ALTER TABLE `memory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motherboard`
--

DROP TABLE IF EXISTS `motherboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `motherboard` (
  `Name` varchar(50) DEFAULT NULL,
  `Socket` varchar(20) DEFAULT NULL,
  `FormFactor` varchar(20) DEFAULT NULL,
  `MemType` varchar(20) DEFAULT NULL,
  `Model` varchar(20) NOT NULL DEFAULT '',
  `Price` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`Model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motherboard`
--

LOCK TABLES `motherboard` WRITE;
/*!40000 ALTER TABLE `motherboard` DISABLE KEYS */;
INSERT INTO `motherboard` VALUES ('Gigabyte GA H110M','Socket 1151','ATX','ddr4','MB-110',4000.00),('Asus Z170 Pro','Socket 1151','ATX','ddr4','MB-190',6000.00),('Gigabyte Z390 Gaming X','Socket 1151','ATX','ddr4','MB-192',11000.00),('MSI X299 Raider','Socket 2066','ATX','ddr4','MB-290',15000.00),('Asus Prime X299 Delux','Socket 2066','ATX','ddr4','MB-291',28000.00),('Asus Tuf X299 Mark2','Socket 2066','ATX','ddr4','MB-292',32000.00),('Gigabyte B450M WiFi','AM4','mATX','ddr4','MB-450',7500.00),('Gigabyte Z490 Aorus Pro AX','Socket 1200','ATX','ddr4','MB-490',30000.00),('Asus ROG Strix Z490','Socket 1200','ATX','ddr4','MB-491',23000.00),('Gigabyte H510','Socket 1200','mATX','ddr4','MB-510',7000.00),('MSI B550M WiFi','AM4','mATX','ddr4','MB-550',9500.00),('MSI Mag B550M Mortar Max WiFi','AM4','mATX','ddr4','MB-551',15000.00),('Asus Tuf B550M WiFi','AM4','mATX','ddr4','MB-552',17000.00),('Asus Prime H610-E','Socket 1700','mATX','ddr4','MB-610',7000.00),('MSI Pro H610M WiFi','Socket 1700','mATX','ddr5','MB-611',8500.00),('MSI Pro B650M','AM5','mATX','ddr5','MB-650',11000.00),('Asus Prime B650M','AM5','mATX','ddr5','MB-651',13000.00),('MSI B650M Gaming WiFi','AM5','mATX','ddr5','MB-652',16000.00),('MSI Pro B650P WiFi','AM5','mATX','ddr5','MB-653',20000.00),('Asus ROG Strix B650','AM5','ATX','ddr5','MB-654',29000.00),('Asus Tuf Gaming X670E+','AM5','ATX','ddr5','MB-670',32000.00),('Asus ROG Crosshair X670E','AM5','ATX','ddr5','MB-671',64000.00),('Asus ROG Strix X670E-E','AM5','ATX','ddr5','MB-672',50000.00),('Gigabyte B760M','Socket 1700','mATX','ddr5','MB-760',15000.00),('Gigabyte B760M WiFi','Socket 1700','mATX','ddr5','MB-761',17000.00),('Asus Prime B760M WiFi','Socket 1700','mATX','ddr5','MB-762',15500.00),('Asus Prime B760M-AYW WiFi','Socket 1700','mATX','ddr5','MB-763',12000.00),('Asus ROG Strix B760 WiFi','Socket 1700','ATX','ddr5','MB-764',26000.00),('MSI Pro B760M','Socket 1700','mATX','ddr4','MB-765',8500.00),('MSI Pro B760MP','Socket 1700','ATX','ddr4','MB-766',11500.00),('MSI Pro B760M Bomber WiFi','Socket 1700','ATX','ddr5','MB-767',11900.00),('MSI Mag B760M Mortar WiFi','Socket 1700','mATX','ddr5','MB-768',18000.00),('Gigabyte Z790 UD','Socket 1700','mATX','ddr5','MB-790',21000.00),('Asus Prime Z790P','Socket 1700','ATX','ddr5','MB-791',22000.00),('Asus ROG Strix Z790 WiFi','Socket 1700','ATX','ddr5','MB-792',44000.00),('Asus ROG Strix Z790H WiFi','Socket 1700','ATX','ddr5','MB-793',32000.00),('MSI Z790 Gaming Plus WiFi','Socket 1700','ATX','ddr5','MB-794',25000.00),('MSI Mag Z790 Tomahawk WiFi','Socket 1700','ATX','ddr5','MB-795',32000.00),('MSI Mpg Z790 Edge Ti Max WiFi','Socket 1700','ATX','ddr5','MB-796',40000.00),('MSI Mpg Z790 Carbon Max WiFi II','Socket 1700','ATX','ddr5','MB-797',55000.00),('MSI Mag X870','AM5','ATX','ddr5','MB-870',36000.00);
/*!40000 ALTER TABLE `motherboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `psu`
--

DROP TABLE IF EXISTS `psu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `psu` (
  `Name` varchar(50) DEFAULT NULL,
  `Wattage` varchar(20) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Model` varchar(20) DEFAULT NULL,
  `Certification` varchar(20) DEFAULT NULL,
  `Price` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `psu`
--

LOCK TABLES `psu` WRITE;
/*!40000 ALTER TABLE `psu` DISABLE KEYS */;
INSERT INTO `psu` VALUES ('Coller Master MWE V2','450W','Non-Modular','PS-450','80 + B',3200.00),('Cooler Master MWE V3','550W','Non-Modular','PS-550','80 + B',4000.00),('Crosair CX750','750W','Non-Modular','PS-750','80 + B',6200.00),('Ant Esports RX550','550W','Non-Modular','PS-551','80 + B',2900.00),('Ant Esports RX650','650W','Non-Modular','PS-650','80 + B',3500.00),('Ant Esports FP','650W','Non-Modular','PS-651','80 + B',3800.00),('Ant Esports FG','650W','Non-Modular','PS-652','80 + G',4500.00),('Ant Esports FP','750W','Non-Modular','PS-751','80 + B',4600.00),('Ant Esports FG','750W','Non-Modular','PS-752','80 + G',5200.00),('Ant Esports FG','850W','Non-Modular','PS-850','80 + G',6500.00),('Cooler Master MWE V3','650W','Non-Modular','PS-653','80 + B',5500.00),('Cooler Master MWE V3','750W','Non-Modular','PS-753','80 + B',6500.00),('Cooler Master MWE V2','850W','Non-Modular','PS-851','80 + G',10000.00),('Cooler Master MWE V2','1050W','Non-Modular','PS-100','80 + B',16500.00),('Cooler Master MWE V2','1250W','Non-Modular','PS-120','80 + B',20000.00),('DeepCool PK450D','450W','Non-Modular','PS-451','80 + B',3200.00),('MSI Mag A550BN','550W','Non-Modular','PS-552','80 + B',3800.00),('DeepCool PL500D','550W','Non-Modular','PS-553','80 + B',3800.00),('Corsair CX550','550W','Non-Modular','PS-554','80 + B',4000.00),('DeepCool PF650','650W','Non-Modular','PS-654','80 + St',3900.00),('DeepCool PL650','650W','Non-Modular','PS-655','80 + B',4700.00),('MSI Mag A650BN','650W','Non-Modular','PS-656','80 + B',4700.00),('Gigabyte P650','650W','Non-Modular','PS-657','80 + S',4700.00),('Gigabyte P650G','650W','Non-Modular','PS-658','80 + G',5000.00),('Antec G650','650W','Semi-Modular','PS-659','80 + G',5300.00),('Antec CSK','750W','Non-Modular','PS-754','80 + B',5500.00),('DeepCool PL','750W','Non-Modular','PS-755','80 + B',5500.00),('Gigabyte UD','750W','Fully-Modular','PS-756','80 + G',7500.00),('MSI Mag A750GL','750W','Fully-Modular','PS-757','80 + G',7600.00),('Corsair','850W','Fully-Modular','PS-852','80 + G',11000.00),('MSI Mag A850GL','850W','Fully-Modular','PS-853','80 + G',8800.00),('Gigabyte UD','850W','Fully-Modular','PS-854','80 + G',9000.00),('Super Flower Leadex','850W','Fully-Modular','PS-855','80 + P',9100.00);
/*!40000 ALTER TABLE `psu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storages`
--

DROP TABLE IF EXISTS `storages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `storages` (
  `Name` varchar(50) DEFAULT NULL,
  `Capacity` varchar(20) DEFAULT NULL,
  `Type` varchar(20) DEFAULT NULL,
  `Generation` varchar(20) DEFAULT NULL,
  `Model` varchar(20) NOT NULL DEFAULT '',
  `Price` decimal(12,2) DEFAULT NULL,
  PRIMARY KEY (`Model`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storages`
--

LOCK TABLES `storages` WRITE;
/*!40000 ALTER TABLE `storages` DISABLE KEYS */;
INSERT INTO `storages` VALUES ('Western Digital Blue 7200RPM','1024GB','HDD','Gen 2','H-100',4500.00),('Western Digital Blue 7200RPM','2048GB','HDD','Gen 2','H-200',5800.00),('Western Digital Blue 5400RPM','4096GB','HDD','Gen 2','H-400',9800.00),('Kingston KC3000','500GB','NVMe M.2','Gen 4','M-350',5000.00),('Kingston KC3000','1024GB','NVMe M.2','Gen 4','M-351',8000.00),('Kingston Fury Renegade','1024GB','NVMe M.2','Gen 4','M-352',9200.00),('Kingston Fury Renegade','2048GB','NVMe M.2','Gen 4','M-353',15000.00),('Kingston Fury Renegade','4096GB','NVMe M.2','Gen 4','M-354',32000.00),('Crucial P3 Plus','500GB','NVMe M.2','Gen 3','M-500',3000.00),('Crucial P3 Plus','1024GB','NVMe M.2','Gen 4','M-501',5500.00),('Adata XPG Gammix S50','1024GB','NVMe M.2','Gen 4','M-700',5000.00),('Adata XPG Gammix S60','500GB','NVMe M.2','Gen 4','M-701',3800.00),('Acer Predator GM7000','1024GB','NVMe M.2','Gen 4','M-709',8200.00),('Samsung 990 Evo','1024GB','NVMe M.2','Gen 4','M-990',9000.00),('Samsung 990 Pro','1024GB','NVMe M.2','Gen 4','M-991',11000.00),('Samsung 990 Pro','2048GB','NVMe M.2','Gen 4','M-992',18000.00),('EVM','128GB','Sata SSD','Gen 3','S-120',1100.00),('Crucial BX500','240GB','Sata SSD','Gen 3','S-502',1500.00),('Crucial BX500','500GB','Sata SSD','Gen 3','S-503',2500.00),('Crucial BX500','1024GB','Sata SSD','Gen 3','S-504',5000.00);
/*!40000 ALTER TABLE `storages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `Name` varchar(30) DEFAULT NULL,
  `Username` varchar(30) DEFAULT NULL,
  `Password` varchar(30) DEFAULT NULL,
  `Email` varchar(30) DEFAULT NULL,
  `SignedUpOn` date DEFAULT NULL,
  `SignedUpAt` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `users_pc`
--

DROP TABLE IF EXISTS `users_pc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users_pc` (
  `Username` varchar(30) DEFAULT NULL,
  `CPU` varchar(50) DEFAULT NULL,
  `GPU` varchar(50) DEFAULT NULL,
  `MotherBoard` varchar(50) DEFAULT NULL,
  `MemModule` varchar(50) DEFAULT NULL,
  `NumberOfModule` int(11) DEFAULT NULL,
  `StorageCapcity` varchar(30) DEFAULT NULL,
  `PSU` varchar(50) DEFAULT NULL,
  `TotalPrice` decimal(12,2) DEFAULT NULL,
  `Date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_pc`
--

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-24  7:43:19
