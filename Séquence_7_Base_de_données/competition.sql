.open "CLUB_KARATE";

CREATE TABLE CATEGORIE (
    num_categorie INT PRIMARY KEY NOT NULL,
    couleur_ceinture VARCHAR(255) NOT NULL,
	katas VARCHAR(255) NOT NULL
);

CREATE TABLE COMPETITION (
    num_competition INT PRIMARY KEY NOT NULL,
    intitule VARCHAR(255) NOT NULL,
	date_competition DATE NOT NULL,
	lieu VARCHAR(255) NOT NULL
);

CREATE TABLE MEMBRE (
    num_membre VARCHAR(42) PRIMARY KEY NOT NULL,
    nom VARCHAR(255) NOT NULL,
	prenom VARCHAR(255) NOT NULL,
	adresse VARCHAR(255) NOT NULL,
    num_categorie INT,
	FOREIGN KEY (num_categorie), REFERENCES CATEGORIE (num_categorie)
);

CREATE TABLE FAIRE_RESULTAT (
    num_membre VARCHAR(42),
    num_competition INT,
    place VARCHAR(255) NOT NULL,
    PRIMARY KEY (num_membre, num_competition),
    FOREIGN KEY (num_membre) REFERENCES MEMBRE(num_membre),
    FOREIGN KEY (num_competition) REFERENCES COMPETITION(num_competition)
);