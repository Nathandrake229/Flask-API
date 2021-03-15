from audio_file import *
import datetime


# route to get all movies
@app.route('/<string:audio_file_type>', methods=['GET'])
def get_data(audio_file_type):
    if(audio_file_type == 'song'):
        return jsonify({'Songs': Song.get_all_songs()})
    if(audio_file_type == 'audiobook'):
        return jsonify({'Audiobooks': Audiobook.get_all_audiobooks()})
    if(audio_file_type == 'podcast'):
        podcast = Podcast.get_all_podcasts()
        for i in podcast:
            st = i['participants']
            i['participants'] = st.split(',')[0:-1]
        return jsonify({'Podcasts': podcast})


# route to get movie by id
@app.route('/<string:audio_file_type>/<int:id>', methods=['GET'])
def get_data_by_id(audio_file_type, id):
    try:
        if(audio_file_type == 'song'):
            return_value = Song.get_song(id)
        if(audio_file_type == 'audiobook'):
            return_value = Audiobook.get_audiobook(id)
        if(audio_file_type == 'podcast'):
            podcast = Podcast.get_podcast(id)
            for i in podcast:
                st = i['participants']
                i['participants'] = st.split(',')[0:-1]
            return_value = podcast
        return jsonify(return_value)
    except:
        response = Response("400 Bad Request", 400, mimetype='application/json')
        return response

# route to add new movie
@app.route('/add/<string:audio_file_type>', methods=['POST'])
def add_data(audio_file_type):
    request_data = request.get_json()  # getting data from client
    try:
        meta = request_data['metadata']
        #meta = request_data['metadata']
        #print(request_data['metadata']['title'])
        #print(request_data['audio_file_type'])
        if(audio_file_type == 'song'):
            
            
            Song.add_song(meta["title"], meta["duration"],
                            meta["upload_time"])
        if(audio_file_type == 'audiobook'):
            
            Audiobook.add_audiobook(meta["title"], meta["duration"],
                            meta["upload_time"], meta["author"], 
                            meta["narrator"])
        if(audio_file_type == 'podcast'):
            participant_string = ""
            if(len(meta["participants"]) <= 10):
                for i in meta["participants"]:
                    if(len(i)<=100):
                        participant_string += i + ", "
                    else:
                        response = Response("400 Bad Request", 400, mimetype='application/json')
                        return response
            else:
                response = Response("400 Bad Request", 400, mimetype='application/json')
                return response
            
            Podcast.add_podcast(meta["title"], meta["duration"],
                            meta["upload_time"], meta["host"], 
                            participant_string)
        response = Response(audio_file_type + " added 200 OK", 200, mimetype='application/json')
    except:
        response = Response("400 Bad Request", 400, mimetype='application/json')
    return response

# route to update movie with PUT method
@app.route('/<string:audio_file_type>/<int:id>', methods=['PUT'])
def update_data(audio_file_type, id):
    request_data = request.get_json()
    request_data = request_data['metadata']
    if(audio_file_type == 'song'):
        Song.update_song(id, request_data['title'], request_data['duration'], 
                        request_data['upload_time'])
    if(audio_file_type == 'audiobook'):
        Audiobook.update_audiobook(id, request_data['title'], request_data['duration'], 
                        request_data['upload_time'], request_data['author'], request_data['narrator'])
    if(audio_file_type == 'podcast'):
        try:
            Podcast.update_podcast(id, request_data['title'], request_data['duration'], 
                            request_data['upload_time'], request_data['host'], request_data['participants'])
            response = Response(audio_file_type + " Updated 200 OK", status=200, mimetype='application/json')
        except:
            response = Response("400 bad request", status=400, mimetype='application/json')
            
    
    return response

# route to delete movie using the DELETE method
@app.route('/<string:audio_file_type>/<int:id>', methods=['DELETE'])
def remove_data(audio_file_type, id):
    try:
        if(audio_file_type == 'song'):
            Song.delete_song(id)
        if(audio_file_type == 'audiobook'):
            Audiobook.delete_audiobook(id)
        if(audio_file_type == 'podcast'):
            Podcast.delete_podcast(id)
        response = Response(audio_file_type + " Deleted", status=200, mimetype='application/json')
    except:
        response = Response("400 Bad Request", 400, mimetype='application/json')
    return response



@app.errorhandler(Exception)
def internal_error(error):

    return "500 Internal Server Error"




if __name__ == "__main__":
    app.run(port=1234, debug=True)