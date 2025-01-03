DROP TABLE  IF EXISTS emprunt;
DROP TABLE  IF EXISTS auteur_de;
DROP TABLE  IF EXISTS auteur;
DROP TABLE  IF EXISTS livre;
DROP TABLE  IF EXISTS usager;

CREATE TABLE usager ( 
					code_barre CHAR(15) PRIMARY KEY,
					nom VARCHAR(90) NOT NULL,
					prenom VARCHAR(90) NOT NULL,
					adresse VARCHAR(300) NOT NULL,
					cp VARCHAR(5) NOT NULL,
					ville VARCHAR(60) NOT NULL,
					email VARCHAR(60) NOT NULL
					);

CREATE TABLE livre ( 
					isbn CHAR(14) PRIMARY KEY,
					titre VARCHAR(300) NOT NULL,
					editeur VARCHAR(90) NOT NULL,
					annee INT NOT NULL
					);
					
CREATE TABLE auteur ( 
					a_id INTEGER PRIMARY KEY AUTOINCREMENT,
					nom VARCHAR(90) NOT NULL,
					prenom VARCHAR(90) NOT NULL
					);	

CREATE TABLE auteur_de ( 
					a_id INTEGER REFERENCES auteur(a_id),
					isbn CHAR(14) REFERENCES livre(isbn),
					PRIMARY KEY (a_id, isbn)
					);

CREATE TABLE emprunt ( 
					code_barre CHAR(15) REFERENCES usager(code_barre),
					isbn CHAR(14)  REFERENCES livre(isbn),
					retour DATE,
					PRIMARY KEY (code_barre, isbn)
					);	


INSERT INTO livre VALUES
-- Livres à partir de 1990
('978-2070541270', 'Harry Potter à l''école des sorciers', 'Gallimard Jeunesse', 1997),
('978-2070643028', 'La Ligne verte', 'Albin Michel', 1996),
('978-2290349229', 'Le Trône de fer', 'J''ai lu', 1998),
('978-2266087308', 'Jurassic Park', 'Pocket', 1990),
('978-2253151432', 'Extension du domaine de la lutte', 'J''ai lu', 1994),
('978-2253155836', 'Un truc soi-disant super auquel on ne me reprendra pas', 'Le Livre de Poche', 1997),
('978-2070417742', 'Les Émigrants', 'Gallimard', 1992),
('978-2020386517', 'Outremonde', 'Seuil', 1997),
('978-2253933137', 'La Transparence du mal', 'Le Livre de Poche', 1990),
('978-2020134613', 'Opération Shylock', 'Seuil', 1993),

-- Livres entre 1970 et 1980
('978-2070293229', 'La Vie mode d''emploi', 'Gallimard', 1978),
('978-2020238113', 'Si par une nuit d''hiver un voyageur', 'Seuil', 1979),
('978-2070367627', 'L''Homme-dé', 'Gallimard', 1971),
('978-2253010692', 'La Tante Julia et le scribouillard', 'Le Livre de Poche', 1977),
('978-2070293704', 'Le Dépeupleur', 'Éditions de Minuit', 1970),
('978-2070386680', 'La Femme gauchère', 'Gallimard', 1978),
('978-2070293698', 'Projet pour une révolution à New York', 'Éditions de Minuit', 1970),
('978-2253014706', 'La Valse aux adieux', 'Le Livre de Poche', 1972),
('978-2020134620', 'Le Système périodique', 'Seuil', 1975),
('978-2253933144', 'L''Établi', 'Le Livre de Poche', 1978),

-- Série Astérix
('978-2012101333', 'Astérix le Gaulois', 'Dargaud', 1961),
('978-2012101340', 'Astérix et Cléopâtre', 'Dargaud', 1965),
('978-2012101357', 'Astérix chez les Bretons', 'Dargaud', 1966),
('978-2012101364', 'Astérix et les Normands', 'Dargaud', 1967),
('978-2012101371', 'Le Tour de Gaule d''Astérix', 'Dargaud', 1965),
('978-2012101388', 'Astérix légionnaire', 'Dargaud', 1967),
('978-2012101395', 'Le Combat des chefs', 'Dargaud', 1966),
('978-2012101401', 'Astérix aux Jeux olympiques', 'Dargaud', 1968);



INSERT INTO usager (code_barre, nom, prenom, adresse, cp, ville, email) VALUES
('U001', 'Dupont', 'Jean', '1 rue de la Paix', '75001', 'Paris', 'jean.dupont@email.com'),
('U002', 'Martin', 'Marie', '15 avenue des Champs-Élysées', '75008', 'Paris', 'marie.martin@email.com'),
('U003', 'Dubois', 'Pierre', '7 place Bellecour', '69002', 'Lyon', 'pierre.dubois@email.com'),
('U004', 'Lefebvre', 'Sophie', '22 rue du Vieux Port', '13002', 'Marseille', 'sophie.lefebvre@email.com'),
('U005', 'Garcia', 'Lucas', '3 rue du Taur', '31000', 'Toulouse', 'lucas.garcia@email.com'),
('U006', 'Laforet', 'Jean', '15 rue Molière', '75002', 'Paris', 'jean.laforet@email.com');


INSERT INTO auteur (nom, prenom) VALUES
('Rowling', 'J.K.'),
('King', 'Stephen'),
('Martin', 'George R.R.'),
('Crichton', 'Michael'),
('Houellebecq', 'Michel'),
('Perec', 'Georges'),
('Calvino', 'Italo'),
('Goscinny', 'René'),
('Uderzo', 'Albert');


INSERT INTO auteur_de (a_id, isbn) VALUES
(1, '978-2070541270'),
(2, '978-2070643028'),
(3, '978-2290349229'),
(4, '978-2266087308'),
(5, '978-2253151432'),
(6, '978-2070293229'),
(7, '978-2020238113'),
(8, '978-2012101333'),
(8, '978-2012101340'),
(8, '978-2012101357'),
(8, '978-2012101364'),
(8, '978-2012101371'),
(8, '978-2012101388'),
(8, '978-2012101395'),
(8, '978-2012101401'),
(9, '978-2012101333'),
(9, '978-2012101340'),
(9, '978-2012101357'),
(9, '978-2012101364'),
(9, '978-2012101371'),
(9, '978-2012101388'),
(9, '978-2012101395'),
(9, '978-2012101401');



INSERT INTO emprunt (code_barre, isbn, retour) VALUES
('U001', '978-2070541270', '2025-01-15'),
('U002', '978-2070643028', '2025-01-20'),
('U003', '978-2290349229', '2025-01-25'),
('U004', '978-2266087308', '2025-01-30'),
('U005', '978-2253151432', '2025-02-05'),
('U001', '978-2012101333', '2025-02-10'),
('U002', '978-2012101340', '2025-02-15'),
('U003', '978-2070293229', '2025-02-20');