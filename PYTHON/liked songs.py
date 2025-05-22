# LIKED SONGS
liked_songs = {
  'Rich as hell':'NBA YB\n',
  'Reflections':'Neighbourhood\n',
  'Drac Woody':'Glokk40spazz',
  'Dope Love':'Gucci Mane',
}
def write_liked_songs_to_file(liked_songs):
  with open('songs.txt','w')as file:
    for song,artist in liked_songs.items():
      file.write(f'{song}-{artist}\n')
    with open('songs.txt','r')as file:
      content = file.read()
      print(content)

write_liked_songs_to_file(liked_songs)


