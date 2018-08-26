from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Genre, Book

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Initialising some dummy users

User1 = User(name="Rize Kamishiro", email="rize@fakemail.com",
             picture='https://vignette.wikia.nocookie.net/thetokyoghoul/\
             images/6/6a/Rize_Kamishiro_Profile.png/revision/latest?cb=\
             20150715151145')
session.add(User1)
session.commit()

User2 = User(name="Light Yagami", email="lyagami@fakemail.com",
             picture='https://imgix.ranker.com/user_node_img/50081/\
             1001613426/original/i-and-_39_ll-take-a-potato-chip-and\
             -eat-it-photo-u1?w=650&q=50&fm=jpg&fit=crop&crop=faces')
session.add(User2)
session.commit()

User3 = User(name="Mayuri Shiina", email="mayuri@fakemail.com",
             picture='https://sep.yimg.com/ay/yhst-91547409642223/steins\
             -gate-mayuri-shiina-cosplay-13.gif')
session.add(User3)
session.commit()


# Adding genres

Fantasy = Genre(name="Fantasy",
                icon='https://is5-ssl.mzstatic.com/image/thumb/Purple\
                122/v4/79/8c/df/798cdfed-8d1f-1cab-be14-89d761e9b4c8/source\
                /256x256bb.jpg')
session.add(Fantasy)
session.commit()

ScienceFiction = Genre(name="Science Fiction",
                       icon='https://is5-ssl.mzstatic.com/image/thumb\
                       /Purple62/v4/0e/54/f8/0e54f841-d25e-788f-68d9\
                       -459cf5bb0b66/source256x256bb.jpg')
session.add(ScienceFiction)
session.commit()

Classics = Genre(name="Classics",
                 icon='https://aardvarkian.files.wordpress.com/2011\
                 /10/56_classics_431.jpg')
session.add(Classics)
session.commit()

Humor = Genre(name="Humor",
              icon='https://www.marketingfacts.nl/images/uploads/jeeves.jpg')
session.add(Humor)
session.commit()

Mystery = Genre(name="Mystery",
                icon='https://is3-ssl.mzstatic.com/image/thumb/Purple128\
                /v4/d2/32/c9/d232c9b9-cc4d-5c87-fa0c-fb0e6833c64a\
                /source/256x256bb.jpg')
session.add(Mystery)
session.commit()

Biography = Genre(name="Biography",
                  icon='https://tse.mm.bing.net/th?id=OIP.nbGs\
                  UD3Rs1_kYypqsaZ3XQAAAA')
session.add(Biography)
session.commit()

SelfHelp = Genre(name="Self Help",
                 icon='https://cdn.24.co.za/files/Cms/General\
                 /d/4482/dc628be03e8744118b959fcc2ad2ca43.jpg')
session.add(SelfHelp)
session.commit()


# Adding some Books

book1 = Book(name="Game of Thrones: A Song of Ice and Fire",
             author="George R R Martin",
             description="A Song of Ice and Fire takes place in a fictional \
             world in which seasons last for years and end unpredictably.The \
             principal story chronicles the power struggle for the Iron \
             Throne among the great Houses of Westeros following \
             the death of King Robert.",
             cover='https://upload.wikimedia.org/wikipedia/en/d/dc\
             /A_Song_of_Ice_and_Fire_book_collection_box_set_cover.jpg',
             genre=Fantasy, user=User1)
session.add(book1)
session.commit()

book2 = Book(name="The Hobbit",
             author="J R R Tolkein",
             description="The Hobbit is set in a time between the Dawn of \
             Faerie and the Dominion of Men, and follows the quest of \
             home-loving hobbit Bilbo Baggins to win a share of the treasure \
             guarded by Smaug the dragon.",
             cover='http://t3.gstatic.com/images?q=tbn:ANd9GcQzlnFVCU2\
             ZcD1K0_5dHip_Uv-fIMCAx3i10XbqWgKLZO9GouV6',
             genre=Fantasy, user=User2)
session.add(book2)
session.commit()

book3 = Book(name="I, Robot", author="Isaac Asimov",
             description="I, Robot is a fixup of science fiction short \
             stories or essays by American writer Isaac Asimov. Although the \
             stories can be read separately, they share a theme of the \
             interaction of humans, robots, and morality, and when combined \
             they tell a larger story of Asimov's fictional \
             history of robotics.",
             cover='https://upload.wikimedia.org/wikipedia/en/d/d5\
             /I_robot.jpg',
             genre=ScienceFiction, user=User3)
session.add(book3)
session.commit()

book4 = Book(name="Journey to the Center of the Earth", author="Jules Verne",
             description="The story involves German professor Otto Lidenbrock \
             who believes there are volcanic tubes going toward the centre of \
             the Earth. He, his nephew Axel, and their guide Hans descend \
             into the Icelandic volcano Snaefellsjokull, encountering many \
             adventures",
             cover='https://upload.wikimedia.org/wikipedia/commons\
             /thumb/6/67/A_Journey_to_the_Centre_of_the_Earth-1874.jpg\
             /330px-A_Journey_to_the_Centre_of_the_Earth-1874.jpg',
             genre=ScienceFiction, user=User1)
session.add(book4)
session.commit()

book5 = Book(name="Pride and Prejudice", author="Jane Austen",
             description="The story charts the emotional development of the \
             protagonist, Elizabeth Bennet, who learns the error of making \
             hasty judgments and comes to appreciate the difference between \
             the superficial and the essential.",
             cover='https://upload.wikimedia.org/wikipedia/commons\
             /thumb/1/17/PrideAndPrejudiceTitlePage.jpg/330px\
             -PrideAndPrejudiceTitlePage.jpg',
             genre=Classics, user=User2)
session.add(book5)
session.commit()

book6 = Book(name="Jane Eyre", author="Charlotte Bronte",
             description="Jane Eyre follows the experiences of its \
             eponymous heroine, including her growth to adulthood and her \
            love for Mr. Rochester, the brooding master of Thornfield Hall. \
            The novel revolutionized prose fiction in that the focus on \
            Jane's moral and spiritual development is told through an \
            intimate, first-person narrative, where actions and events are \
            coloured by a psychological intensity.",
             cover='https://upload.wikimedia.org/wikipedia/commons/thumb\
             /9/9b/Jane_Eyre_title_page.jpg/330px-Jane_Eyre_title_page.jpg',
             genre=Classics, user=User3)
session.add(book6)
session.commit()

book7 = Book(name="Right Ho Jeeves", author="P G Wodehouse",
             description="Right Ho, Jeeves is a novel by P. G. Wodehouse, \
             the second full-length novel featuring the popular characters \
             Jeeves and Bertie Wooster, after Thank You, Jeeves.",
             cover='https://upload.wikimedia.org/wikipedia/en/8/83\
             /RightHoJeeves.jpg',
             genre=Humor, user=User1)
session.add(book7)
session.commit()

book8 = Book(name="Three Men in a Boat", author="Jerome K Jerome",
             description="This is a humorous account by English writer \
             Jerome K. Jerome of a two-week boating holiday on the Thames \
             from Kingston upon Thames to Oxford and back to Kingston.",
             cover='https://images-na.ssl-images-amazon.com/images\
             /I/71iCUnY11ML.jpg',
             genre=Humor, user=User2)
session.add(book8)
session.commit()

book9 = Book(name="The Murder at the Vicarge", author="Agatha Christie",
             description="In St. Mary Mead, no one is more despised than \
             Colonel Lucius Protheroe. Even the local vicar has said that \
             killing him would be doing a service to the townsfolk. \
             So when Protheroe is found murdered in the same vicar's study, \
             and two different people confess to the crime, it is time for \
             the elderly spinster Jane Marple to exercise her \
             detecting abilities. ",
             cover='https://upload.wikimedia.org/wikipedia/en/b/bf\
             /The_Murder_at_the_Vicarage_First_Edition_Cover_1930.jpg',
             genre=Mystery, user=User3)
session.add(book9)
session.commit()

book10 = Book(name="Gone Girl", author="Gillian Flynn",
              description="This novel's suspense comes from the main character \
              Nick Dunne, and whether he is involved in the disappearance \
              of his wife.",
              cover='https://images-na.ssl-images-amazon.com/images/I\
              /516Gb2s1eGL._SX324_BO1,204,203,200_.jpg',
              genre=Mystery, user=User1)
session.add(book10)
session.commit()

book11 = Book(name="When Breath Becomes Air", author="Paul Kalanithi",
              description="When Breath Becomes Air is a non-fiction \
              autobiographical book written by Paul Kalanithi. It is a \
              memoir about his life and illness, battling stage IV metastatic \
              lung cancer. It was posthumously published by Random House on \
              January 12, 2016.",
              cover='https://upload.wikimedia.org/wikipedia/en/d/dd\
              /When_Breath_Becomes_Air.jpg',
              genre=Biography, user=User2)
session.add(book11)
session.commit()

book12 = Book(name="Steve Jobs", author="Walter Isaacson",
              description="Based on more than forty interviews with Jobs \
              conducted over two years in addition to interviews with \
              more than one hundred family members, friends, adversaries, \
              competitors, and colleagues; Isaacson gives unprecedented \
              access to Jobs's life",
              cover='https://upload.wikimedia.org/wikipedia/en/e/e4\
              /Steve_Jobs_by_Walter_Isaacson.jpg',
              genre=Biography, user=User3)
session.add(book12)
session.commit()

book13 = Book(name="Thinking Fast and Slow", author="Daniel Kahneman",
              description="The central thesis is a dichotomy between two modes \
              of thought: System 1 is fast, instinctive and emotional; \
              System 2 is slower, more deliberative, and more logical. \
              The book delineates cognitive biases linked with each type of \
              thinking, starting with Kahneman's own research on loss \
              aversion.",
              cover='https://upload.wikimedia.org/wikipedia/en/c/c1\
              /Thinking%2C_Fast_and_Slow.jpg',
              genre=SelfHelp, user=User1)
session.add(book13)
session.commit()

book14 = Book(name="7 Habits of Highly Effective People",
              author="Steven R Covey",
              description="Covey presents an approach to being effective in \
              attaining goals by aligning oneself to what he calls true north \
              principles based on a character ethic that he presents as \
              universal and timeless.",
              cover='https://upload.wikimedia.org/wikipedia/en/a/a2\
              /The_7_Habits_of_Highly_Effective_People.jpg',
              genre=SelfHelp, user=User2)
session.add(book14)
session.commit()


print "Initialised the database"
