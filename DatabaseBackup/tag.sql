-- MySQL dump 10.13  Distrib 8.0.12, for Win64 (x86_64)
--
-- Host: localhost    Database: project
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `tag` (
  `tag` varchar(50) NOT NULL,
  PRIMARY KEY (`tag`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES ('1980s'),('1990\'s'),('2.5D'),('2D'),('2D Fighter'),('360 Video'),('3D Platformer'),('3D Vision'),('4 Player Local'),('4X'),('6DOF'),('Abstract'),('Action'),('Action RPG'),('Action-Adventure'),('Adventure'),('Agriculture'),('Aliens'),('Alternate History'),('America'),('Animation & Modeling'),('Anime'),('Arcade'),('Arena Shooter'),('Artificial Intelligence'),('Assassin'),('Asynchronous Multiplayer'),('Atmospheric'),('Audio Production'),('Base-Building'),('Based On A Novel'),('Basketball'),('Batman'),('Beat\'em up'),('Benchmark'),('Bikes'),('Blood'),('Board Game'),('Bowling'),('Building'),('Bullet Hell'),('Bullet Time'),('Capitalism'),('Card Game'),('Cartoon'),('Cartoony'),('Casual'),('Character Action Game'),('Character Customization'),('Chess'),('Choices Matter'),('Choose Your Own Adventure'),('Cinematic'),('City Builder'),('Class-Based'),('Classic'),('Clicker'),('Co-op'),('Co-op Campaign'),('Cold War'),('Colorful'),('Comedy'),('Comic Book'),('Competitive'),('Conspiracy'),('Controller'),('Conversation'),('Crafting'),('Crime'),('Crowdfunded'),('CRPG'),('Cult Classic'),('Cute'),('Cyberpunk'),('Cycling'),('Dark'),('Dark Comedy'),('Dark Fantasy'),('Dark Humor'),('Dating Sim'),('Demons'),('Design & Illustration'),('Destruction'),('Detective'),('Difficult'),('Dinosaurs'),('Diplomacy'),('Documentary'),('Dragons'),('Drama'),('Driving'),('Dungeon Crawler'),('Dynamic Narration'),('Dystopian'),('e-sports'),('Early Access'),('Economy'),('Education'),('Episodic'),('Experience'),('Experimental'),('Exploration'),('Faith'),('Family Friendly'),('Fantasy'),('Fast-Paced'),('Female Protagonist'),('Fighting'),('First-Person'),('Fishing'),('Flight'),('FMV'),('Football'),('FPS'),('Free to Play'),('Funny'),('Futuristic'),('Gambling'),('Game Development'),('GameMaker'),('Games Workshop'),('Gaming'),('God Game'),('Golf'),('Gore'),('Gothic'),('Grand Strategy'),('Great Soundtrack'),('Grid-Based Movement'),('Gun Customization'),('Hack and Slash'),('Hacking'),('Hand-drawn'),('Hardware'),('Heist'),('Hex Grid'),('Hidden Object'),('Historical'),('Horror'),('Horses'),('Hunting'),('Illuminati'),('Indie'),('Intentionally Awkward Controls'),('Interactive Fiction'),('Inventory Management'),('Investigation'),('Isometric'),('JRPG'),('Kickstarter'),('Lara Croft'),('LEGO'),('Lemmings'),('Level Editor'),('Linear'),('Local Co-Op'),('Local Multiplayer'),('Logic'),('Loot'),('Lore-Rich'),('Lovecraftian'),('Magic'),('Management'),('Mars'),('Martial Arts'),('Massively Multiplayer'),('Match 3'),('Mature'),('Mechs'),('Medieval'),('Memes'),('Metroidvania'),('Military'),('Mini Golf'),('Minimalist'),('Mining'),('MMORPG'),('MOBA'),('Mod'),('Moddable'),('Modern'),('Mouse only'),('Movie'),('Multiplayer'),('Multiple Endings'),('Music'),('Music-Based Procedural Generation'),('Mystery'),('Mystery Dungeon'),('Mythology'),('Narration'),('Naval'),('Ninja'),('Noir'),('Nonlinear'),('NSFW'),('Nudity'),('Offroad'),('On-Rails Shooter'),('Online Co-Op'),('Open World'),('Otome'),('Parkour'),('Parody'),('Party-Based RPG'),('Perma Death'),('Philisophical'),('Photo Editing'),('Physics'),('Pinball'),('Pirates'),('Pixel Graphics'),('Platformer'),('Point & Click'),('Political'),('Politics'),('Pool'),('Post-apocalyptic'),('Procedural Generation'),('Programming'),('Psychedelic'),('Psychological'),('Psychological Horror'),('Puzzle'),('Puzzle-Platformer'),('PvE'),('PvP'),('Quick-Time Events'),('Racing'),('Real Time Tactics'),('Real-Time'),('Real-Time with Pause'),('Realistic'),('Relaxing'),('Remake'),('Replay Value'),('Resource Management'),('Retro'),('Rhythm'),('Robots'),('Rogue-like'),('Rogue-lite'),('Romance'),('Rome'),('RPG'),('RPGMaker'),('RTS'),('Runner'),('Sailing'),('Sandbox'),('Satire'),('Sci-fi'),('Science'),('Score Attack'),('Sexual Content'),('Shoot\'Em Up'),('Shooter'),('Short'),('Side Scroller'),('Silent Protagonist'),('Simulation'),('Singleplayer'),('Sniper'),('Soccer'),('Software'),('Software Training'),('Sokoban'),('Soundtrack'),('Space'),('Space Sim'),('Spectacle Fighter'),('Spelling'),('Split Screen'),('Sports'),('Star Wars'),('Stealth'),('Steam Machine'),('Steampunk'),('Story Rich'),('Strategy'),('Strategy RPG'),('Stylized'),('Superhero'),('Supernatural'),('Surreal'),('Survival'),('Survival Horror'),('Swordplay'),('Tactical'),('Tactical RPG'),('Tading Card Game'),('Tanks'),('Team-Based'),('Text-Based'),('Third Person'),('Third-Person Shooter'),('Thriller'),('Time Attack'),('Time Manipulation'),('Time Travel'),('Top-Down'),('Top-Down Shooter'),('Touch-Friendly'),('Tower Defense'),('TrackIR'),('Trading'),('Trains'),('Transhumanism'),('Turn-Based'),('Turn-Based Combat'),('Turn-Based Strategy'),('Turn-Based Tactics'),('Tutorial'),('Twin Stick Shooter'),('Typing'),('Underground'),('Underwater'),('Utilities'),('Vampire'),('Video Production'),('Villian Protagonist'),('Violent'),('Visual Novel'),('Voice Control'),('Voxel'),('VR'),('VR Only'),('Walking Simulator'),('War'),('Wargame'),('Warhammer 40K'),('Web Publishing'),('Werewolves'),('Western'),('Word Game'),('World War I'),('World War II'),('Wrestling'),('Zombies');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-16 22:01:18
