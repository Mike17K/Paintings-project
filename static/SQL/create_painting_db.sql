CREATE DATABASE `paintings`;
USE `paintings`;
CREATE TABLE `user` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`firstname` VARCHAR(255) NOT NULL,
	`lastname` VARCHAR(255) NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	`photo` INT NULL,
	`region` VARCHAR(255) NOT NULL,
	`sity` VARCHAR(255) NOT NULL,
	`birthdate` DATE NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `message` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`sender` INT NOT NULL,
	`receiver` INT NOT NULL,
	`content` TEXT NOT NULL,
	`timestamp` TIMESTAMP NOT NULL,
	`about` INT NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `payment` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`amount` FLOAT NOT NULL,
	`timestamp` TIMESTAMP NOT NULL,
	`order` INT NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `image` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`photo` blob NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`size` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `order` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`painting` INT NOT NULL,
	`date` DATE NOT NULL,
	`buyer` INT NOT NULL,
	`status` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `painting` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`title` TEXT NOT NULL,
	`width` FLOAT NOT NULL,
	`height` FLOAT NOT NULL,
	`artist` VARCHAR(255) NOT NULL,
	`description` TEXT NOT NULL,
	`type` VARCHAR(255) NOT NULL,
	`location` VARCHAR(255) NOT NULL,
	`yearmade` INT NOT NULL,
	`suportmaterial` VARCHAR(255) NOT NULL,
	`methodcategory` VARCHAR(255) NOT NULL,
	`owner` INT NOT NULL,
	`available` BOOLEAN NOT NULL,
	`img` INT NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `feedback` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`text` TEXT NOT NULL,
	`writer` INT NOT NULL,
	`seller` INT NOT NULL,
	`rating` FLOAT NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `contains` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`msg` INT NOT NULL,
	`img` INT NOT NULL,
	PRIMARY KEY (`id`)
);
CREATE TABLE `forsale` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`painting` INT NOT NULL,
	`price` FLOAT NOT NULL,
	`timestamp` TIMESTAMP NOT NULL,
	`added-description` TEXT NOT NULL,
	`active` BOOLEAN NOT NULL,
	PRIMARY KEY (`id`)
);
ALTER TABLE `user`
ADD CONSTRAINT `user_fk0` FOREIGN KEY (`photo`) REFERENCES `image`(`id`);
ALTER TABLE `message`
ADD CONSTRAINT `message_fk0` FOREIGN KEY (`sender`) REFERENCES `user`(`id`);
ALTER TABLE `message`
ADD CONSTRAINT `message_fk1` FOREIGN KEY (`receiver`) REFERENCES `user`(`id`);
ALTER TABLE `message`
ADD CONSTRAINT `message_fk2` FOREIGN KEY (`about`) REFERENCES `painting`(`id`);
ALTER TABLE `payment`
ADD CONSTRAINT `payment_fk0` FOREIGN KEY (`order`) REFERENCES `order`(`id`);
ALTER TABLE `order`
ADD CONSTRAINT `order_fk0` FOREIGN KEY (`painting`) REFERENCES `forsale`(`id`);
ALTER TABLE `order`
ADD CONSTRAINT `order_fk1` FOREIGN KEY (`buyer`) REFERENCES `user`(`id`);
ALTER TABLE `painting`
ADD CONSTRAINT `painting_fk0` FOREIGN KEY (`owner`) REFERENCES `user`(`id`);
ALTER TABLE `painting`
ADD CONSTRAINT `painting_fk1` FOREIGN KEY (`img`) REFERENCES `image`(`id`);
ALTER TABLE `feedback`
ADD CONSTRAINT `feedback_fk0` FOREIGN KEY (`writer`) REFERENCES `user`(`id`);
ALTER TABLE `feedback`
ADD CONSTRAINT `feedback_fk1` FOREIGN KEY (`seller`) REFERENCES `user`(`id`);
ALTER TABLE `contains`
ADD CONSTRAINT `contains_fk0` FOREIGN KEY (`msg`) REFERENCES `message`(`id`);
ALTER TABLE `contains`
ADD CONSTRAINT `contains_fk1` FOREIGN KEY (`img`) REFERENCES `image`(`id`);
ALTER TABLE `forsale`
ADD CONSTRAINT `forsale_fk0` FOREIGN KEY (`painting`) REFERENCES `painting`(`id`);