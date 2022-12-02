from models import User, Post, db, connect_db, Tag, PostTag
from app import app
import datetime


def reset_to_seed():
        db.drop_all()   
        db.create_all()

        User.query.delete()
        Post.query.delete()

        ##################
        ###### Users

        # id 1
        tau = User(first_name="Alexandretta", last_name="Tau", image_url="https://iili.io/Hf2Ot5b.md.png")
        # id 2
        zhu = User(first_name="Kong", last_name="Zhu", image_url="https://iili.io/HfFcDYB.md.jpg")
        # id 3
        catering = User(first_name="Winslow", last_name="Catering", image_url="https://iili.io/HfFlu44.jpg")
        # id 4
        whitoak = User(first_name="Elisa", last_name="Whitoak", image_url="https://iili.io/HfK31Pj.png")

        db.session.add(tau)
        db.session.add(zhu)
        db.session.add(catering)
        db.session.add(whitoak)

        ##################
        ###### Posts

        # for catering (id 3)
        # post id 1
        p = Post(
                title='My First Post',
                content='Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi.Epsum factorial non deposit quid pro quo hic escorol. Olypian quarrels et gorilla congolium sic ad nauseum.',
                user=User.query.get(3),
                created_at=datetime.datetime(2012, 11, 30, 15, 48, 26, 229857))
        db.session.add(p)
        db.session.commit()

        # for tau (id 1)
        # post id 2
        p = Post(
                title='Test',
                content='Epsum factorial non deposit quid pro quo hic escorol. Olypian quarrels et gorilla congolium sic ad nauseum. Souvlaki ignitus carborundum e pluribus unum. Defacto lingo est igpay atinlay. Marquee selectus non provisio incongruous feline nolo contendre. Gratuitous octopus niacin, sodium glutimate. Quote meon an estimate et non interruptus stadium. Sic tempus fugit esperanto hiccup estrogen. Glorious baklava ex librus hup hey ad infinitum. Non sequitur condominium facile et geranium incognito. Epsum factorial non deposit quid pro quo hic escorol. Marquee selectus non provisio incongruous feline nolo contendre Olypian quarrels et gorilla congolium sic ad nauseum. Souvlaki ignitus carborundum e pluribus.',
                user=User.query.get(1),
                created_at=datetime.datetime(2015, 3, 16, 17, 48, 26, 229857))
        db.session.add(p)
        db.session.commit()

        # post id 3
        p = Post(
                title='Hello',
                content='Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, li tot Europa usa li sam vocabularium. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilita; de un nov lingua franca: on refusa continuar payar custosi traductores. It solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles.Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan.',
                user=User.query.get(1),
                created_at=datetime.datetime(2017, 3, 12, 13, 48, 26, 229857))
        db.session.add(p)
        db.session.commit()

        # for zhu (id 2)
        # post id 4
        p = Post(
                title='First Post Ever',
                content='Epsum factorial non deposit quid pro quo hic escorol. Olypian quarrels et gorilla congolium sic ad nauseum. Souvlaki ignitus carborundum e pluribus unum. Defacto lingo est igpay atinlay. Marquee selectus non provisio incongruous feline nolo contendre. Gratuitous octopus niacin, sodium glutimate. Quote meon an estimate et non interruptus stadium. Sic tempus fugit esperanto hiccup estrogen. Glorious baklava ex librus hup hey ad infinitum. Non sequitur condominium facile et geranium incognito. Epsum factorial non deposit quid pro quo hic escorol. Marquee selectus non provisio incongruous feline nolo contendre Olypian quarrels et gorilla congolium sic ad nauseum. Souvlaki ignitus carborundum e pluribus.',
                user=User.query.get(2),
                created_at=datetime.datetime(2018, 12, 22, 12, 48, 26, 229857))
        db.session.add(p)
        db.session.commit()

        # post id 5
        p = Post(
                title='Let me tell you about my day',
                content='Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, li tot Europa usa li sam vocabularium. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilita; de un nov lingua franca: on refusa continuar payar custosi traductores. It solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles.Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan.',
                user=User.query.get(2),
                created_at=datetime.datetime(2022, 7, 3, 14, 48, 26, 229857))
        db.session.add(p)
        db.session.commit()

        # for whitoak (id 4)
        # post id 6
        p = Post(
                title='Salutations',
                content='Epsum factorial non deposit quid pro quo hic escorol. Olypian quarrels et gorilla congolium sic ad nauseum. Souvlaki ignitus carborundum e pluribus unum. Defacto lingo est igpay atinlay. Marquee selectus non provisio incongruous feline nolo contendre. Gratuitous octopus niacin, sodium glutimate. Quote meon an estimate et non interruptus stadium. Sic tempus fugit esperanto hiccup estrogen. Glorious baklava ex librus hup hey ad infinitum. Non sequitur condominium facile et geranium incognito. Epsum factorial non deposit quid pro quo hic escorol. Marquee selectus non provisio incongruous feline nolo contendre Olypian quarrels et gorilla congolium sic ad nauseum. Souvlaki ignitus carborundum e pluribus.',
                user=User.query.get(4),
                created_at=datetime.datetime(1999, 4, 3, 5, 55, 26, 229857))
        db.session.add(p)
        db.session.commit()

        # post id 7
        p = Post(
                title='My journeys so far...',
                content='Li Europan lingues es membres del sam familie. Lor separat existentie es un myth. Por scientie, musica, sport etc, li tot Europa usa li sam vocabularium. Li lingues differe solmen in li grammatica, li pronunciation e li plu commun vocabules. Omnicos directe al desirabilita; de un nov lingua franca: on refusa continuar payar custosi traductores. It solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles.Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan.',
                user=User.query.get(4),
                created_at=datetime.datetime(1999, 6, 7, 7, 45, 26, 229857))
        db.session.add(p)
        db.session.commit()

        ##################
        ###### Tags

        # tag id 1
        greetings = Tag(name="greeting")
        # tag id 2
        first = Tag(name="first post")
        # tag id 3
        test = Tag(name="test post")

        db.session.add(greetings)
        db.session.add(first)
        db.session.add(test)
        db.session.commit()

        ##################
        ###### Posts Tags

        # tags for post id 1
        t1 = PostTag(post_id='1',tag_id='1')
        t2 = PostTag(post_id='1',tag_id='2')
        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

        # tags for post id 2
        t1 = PostTag(post_id='2',tag_id='3')
        t2 = PostTag(post_id='2',tag_id='2')
        db.session.add(t1)
        db.session.add(t2)
        db.session.commit()

        # tags for post id 3
        t1 = PostTag(post_id='3',tag_id='1')
        db.session.add(t1)
        db.session.commit()
        
reset_to_seed()