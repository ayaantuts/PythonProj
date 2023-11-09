-- Create a new database named "Library"
CREATE DATABASE IF NOT EXISTS Library;

-- Switch to the "Library" database
USE Library;

-- Create the "Book" table
CREATE TABLE IF NOT EXISTS Books (
	bookId INT PRIMARY KEY,
	author VARCHAR(255),
	title VARCHAR(255),
	publishYear INT,
	editionNo INT,
	quantity INT,
	shelfNo INT
);

-- Insert dummy data
INSERT INTO Books VALUES
	(1, "John Doe", "The Great Adventure", 2020, 1, 10, 101),
	(2, "Jane Smith", "Coding 101", 2019, 2, 5, 102),
	(3, "Alice Johnson", "Mystery Mansion", 2022, 1, 8, 103),
	(4, "Bob Williams", "Data Science Handbook", 2021, 3, 12, 104),
	(5, "Eva Davis", "History Unraveled", 2018, 2, 15, 105),
	(6, "Ravi Patel", "The Silent Hills", 2017, 1, 7, 106),
	(7, "Priya Sharma", "Code of Destiny", 2023, 2, 10, 107),
	(8, "Amit Singh", "Infinite Connections", 2019, 1, 5, 108),
	(9, "Kavita Verma", "Whispers of the Soul", 2020, 2, 8, 109),
	(10, "Raj Kapoor", "The Forgotten Empire", 2021, 1, 12, 110),
	(11, "Anita Joshi", "Programming Paradigm", 2018, 3, 15, 111),
	(12, "Vikram Mehta", "Eternal Love", 2022, 2, 9, 112),
	(13, "Suman Khanna", "Beyond the Horizon", 2016, 1, 11, 113),
	(14, "Rahul Kumar", "The Quantum Mind", 2023, 3, 14, 114),
	(15, "Mona Chopra", "Sands of Time", 2015, 2, 6, 115),
	(16, "Deepak Sharma", "Data Analytics Explained", 2020, 1, 8, 116),
	(17, "Neha Gupta", "The Enchanted Forest", 2022, 2, 13, 117),
	(18, "Arun Kumar", "Web Development Unleashed", 2017, 1, 7, 118),
	(19, "Sonia Verma", "In Pursuit of Happiness", 2019, 3, 10, 119),
	(20, "Vivek Singh", "Mystical Realms", 2021, 1, 12, 120),
	(21, "Pooja Kapoor", "Code of the Cosmos", 2018, 2, 15, 121),
	(22, "Sanjay Mehta", "The Art of Programming", 2016, 1, 9, 122),
	(23, "Anjali Saxena", "Echoes of Eternity", 2022, 3, 11, 123),
	(24, "Rahul Verma", "The Lost Civilization", 2017, 2, 14, 124),
	(25, "Sneha Sharma", "Journey to the Stars", 2019, 1, 6, 125),
	(26, "Michael Johnson", "The Future of Artificial Intelligence", 2023, 1, 10, 201),
	(27, "Sophie Müller", "Cybersecurity Essentials", 2022, 2, 8, 202),
	(28, "Hiroshi Tanaka", "Quantum Computing: A Practical Guide", 2021, 1, 12, 203),
	(29, "Olga Petrov", "Blockchain Revolution", 2020, 3, 15, 204),
	(30, "Carlos Rodriguez", "The DevOps Handbook", 2019, 2, 9, 205),
	(31, "Yuki Kato", "Python Mastery", 2018, 1, 11, 206),
	(32, "Emma Smith", "Machine Learning for Beginners", 2017, 2, 14, 207),
	(33, "Chen Wei", "Cloud Computing: The Complete Guide", 2022, 1, 7, 208),
	(34, "Isabella Rossi", "Data Science in Action", 2016, 3, 10, 209),
	(35, "Miguel Hernandez", "The Agile Manifesto", 2020, 1, 12, 210),
	(36, "Aisha Khan", "UX Design Principles", 2019, 2, 15, 211),
	(37, "Kenji Yamamoto", "Mobile App Development 101", 2021, 1, 8, 212),
	(38, "Ananya Patel", "The Internet of Things Revolution", 2018, 2, 13, 213),
	(39, "Sebastian Müller", "Artificial Neural Networks Explained", 2023, 1, 9, 214),
	(40, "Maria Lopez", "Ethical Hacking and Penetration Testing", 2017, 2, 11, 215),
	(41, "Elena Rodriguez", "The Enchanted Kingdom", 2019, 1, 10, 301),
	(42, "Gregor Blackthorn", "Realm of Dragons", 2020, 2, 8, 302),
	(43, "Luna Silvermoon", "The Elven Prophecy", 2021, 1, 12, 303),
	(44, "Xander Darkblade", "Sorcery's Secret", 2018, 3, 15, 304),
	(45, "Aria Nightshade", "Chronicles of the Mystic Isles", 2017, 2, 9, 305),
	(46, "Thorn Ironheart", "The Shadow's Embrace", 2022, 1, 11, 306),
	(47, "Isolde Moonshadow", "Eternal Nightfall", 2016, 2, 14, 307),
	(48, "Gideon Frostfire", "Wizard's Awakening", 2023, 1, 7, 308),
	(49, "Astrid Stormrider", "The Phoenix Crown", 2020, 3, 10, 309),
	(50, "Soren Stormwind", "Tales of the Feywild", 2018, 2, 12, 310),
	(51, "Lyra Moonstone", "The Crystal Labyrinth", 2021, 1, 15, 311),
	(52, "Faelan Starlight", "Dragon's Flight", 2017, 2, 8, 312),
	(53, "Eowyn Silverwind", "The Lost Scepter", 2019, 1, 13, 313),
	(54, "Cedric Shadowcaster", "Whispers of the Ancients", 2022, 2, 10, 314),
	(55, "Morgana Darkheart", "The Cursed Chronicles", 2016, 1, 9, 315),
	(56, "Aerin Firestorm", "The Fey Court Conspiracy", 2023, 3, 11, 316),
	(57, "Thalia Nightshade", "Serpent's Dance", 2017, 2, 14, 317),
	(58, "Kael Sunblade", "Kingdom of Shadows", 2019, 1, 6, 318),
	(59, "Selene Starfall", "The Astral Odyssey", 2020, 2, 11, 319),
	(60, "Darian Frostbane", "The Elemental War", 2018, 3, 12, 320);

SELECT * FROM Books;