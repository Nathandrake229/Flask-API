from settings import *
import json

db = SQLAlchemy(app)


class Song(db.Model):
    __tablename__ = 'audio_file_song'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(100), nullable=False)
    # nullable is false so the column can't be empty
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.String(100), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'duration': self.duration, 'upload_time': self.upload_time}

    def add_song(_title, _duration, _upload_time):
        new_file = Song(title=_title, duration=_duration, upload_time=_upload_time)
        db.session.add(new_file)  
        db.session.commit()  # commit changes to session
        
        print("x")

    def get_all_songs():
        return [Song.json(song) for song in Song.query.all()]

    def get_song(_id):
        return [Song.json(Song.query.filter_by(id=_id).first())]

    def update_song(_id, _title, _duration, _upload_time):
        song_to_update = Song.query.filter_by(id=_id).first()
        song_to_update.title = _title
        song_to_update.duration = _duration
        song_to_update.upload_time = _upload_time
        db.session.commit()

    def delete_song(_id):
        Song.query.filter_by(id=_id).delete()
        db.session.commit()  # commiting the new change to our database


class Audiobook(db.Model):
    __tablename__ = 'audio_file_audiobook'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(100), nullable=False)
    # nullable is false so the column can't be empty
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    narrator = db.Column(db.String(100), nullable=False)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'duration': self.duration, 'upload_time': self.upload_time,
                'author': self.author, 'narrator': self.narrator}

    def add_audiobook(_title, _duration, _upload_time, _author, _narrator):
        new_file = Audiobook(title=_title, duration=_duration, upload_time=_upload_time, author=_author, narrator=_narrator)
        db.session.add(new_file)
        db.session.commit()  # commit changes to session

    def get_all_audiobooks():
        return [Audiobook.json(audiobook) for audiobook in Audiobook.query.all()]

    def get_audiobook(_id):
        return [Audiobook.json(Audiobook.query.filter_by(id=_id).first())]

    def update_audiobook(_id, _title, _duration, _upload_time, _author, _narrator):
        audiobook_to_update = Audiobook.query.filter_by(id=_id).first()
        audiobook_to_update.title = _title
        audiobook_to_update.duration = _duration
        audiobook_to_update.upload_time = _upload_time
        audiobook_to_update.author = _author
        audiobook_to_update.narrator = _narrator
        db.session.commit()

    def delete_audiobook(_id):
        Audiobook.query.filter_by(id=_id).delete()
        db.session.commit()  # commiting the new change to our database


class Podcast(db.Model):
    __tablename__ = 'audio_file_podcast'  # creating a table name
    id = db.Column(db.Integer, primary_key=True)  # this is the primary key
    title = db.Column(db.String(100), nullable=False)
    # nullable is false so the column can't be empty
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.String(100), nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.String(1500), nullable=True)

    def json(self):
        return {'id': self.id, 'title': self.title,
                'duration': self.duration, 'upload_time': self.upload_time,
                'host': self.host, 'participants': self.participants}

    def add_podcast(_title, _duration, _upload_time, _host, _participants):
        new_file = Podcast(title=_title, duration=_duration, upload_time=_upload_time, host=_host, participants=_participants)
        db.session.add(new_file)
        db.session.commit()  # commit changes to session

    def get_all_podcasts():
        return [Podcast.json(podcast) for podcast in Podcast.query.all()]

    def get_podcast(_id):
        return [Podcast.json(Podcast.query.filter_by(id=_id).first())]

    def update_podcast(_id, _title, _duration, _upload_time, _host, _participants):
        podcastto_update = Podcast.query.filter_by(id=_id).first()
        podcast_to_update.title = _title
        podcast_to_update.duration = _duration
        podcast_to_update.upload_time = _upload_time
        podcast_to_update.host = _host
        podcast_to_update.participants = _participants
        db.session.commit()

    def delete_podcast(_id):
        Podcast.query.filter_by(id=_id).delete()
        db.session.commit()  # commiting the new change to our database




db.create_all()

