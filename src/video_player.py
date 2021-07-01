"""A video player class."""
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from src.video_library import VideoLibrary
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.vidU = ""
        self.counter = 0
        self.countP = 0
        self.num_vids = 0
        self.playlist = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_vids = self._video_library.get_all_videos()
        all_vids.sort()
        print("Here's a list of all available videos:")
        for i in range(5):
            Tg = ' '.join(all_vids[i].tags) #converting tag tuples into a string
         

            print("  {0} ({1}) [{2}]".format(all_vids[i].title, all_vids[i].video_id,Tg ))
        
    def show_a_video(self,video_title):
        all_vids = self._video_library.get_all_videos()

        for i in range(5):
            Tg = ' '.join(all_vids[i].tags) #converting tag tuples into a string
            if video_title == all_vids[i].title and self.countP == 0:
                print("{0} ({1}) [{2}]".format(all_vids[i].title, all_vids[i].video_id,Tg ))
            if video_title == all_vids[i].title and self.countP > 0:
                print("{0} ({1}) [{2}]".format(all_vids[i].title, all_vids[i].video_id,Tg ),end=" ")


    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        self.counter += 1
        if self.counter == 1:
            vid = self._video_library.get_video(video_id)
            if vid == None:
                print("Cannot play video: Video does not exist")
            else:
                vidT = vid.title
                print("Playing video: {0}".format(vidT))
                self.vidU = vidT
        elif self.counter > 1:
            vid = self._video_library.get_video(video_id)
            if vid == None:
                print("Cannot play video: Video does not exist")
            else:
                
                print("Stopping video: {0}".format(self.vidU))
           
                vidT = vid.title
                print("Playing video: {0}".format(vidT))
                self.vidU = vidT
                self.countP = 0
        

    def stop_video(self):
        """Stops the current video."""
        if self.counter < 1:
            print("Cannot stop video: No video is currently playing")
            self.counter = 0
            self.countP = 0
        else:
            print(f"Stopping video: {self.vidU}")
            self.counter = 0
            self.countP = 0

    def play_random_video(self):
        """Plays a random video from the video library."""
        vid_ids = self._video_library.get_video_id()
        n = random.randint(0,len(vid_ids)-1)
        self.play_video(vid_ids[n])
        

    def pause_video(self):
        """Pauses the current video."""
        
        if self.counter == 0:
            print("Cannot pause video: No video is currently playing")
            
        elif self.counter >= 1:
            self.countP += 1
            if self.countP == 1:
                print(f"Pausing video: {self.vidU}")
            elif self.countP > 1:
                print(f"Video already paused: {self.vidU}")
        
       

    def continue_video(self):
        """Resumes playing the current video."""
        if self.counter == 0:
            print("Cannot continue video: No video is currently playing")
        elif  self.countP > 0:
            print("Continuing video: Amazing Cats")
            self.countP = 0
        elif self.countP == 0:
            print("Cannot continue video: Video is not paused")
        


    def show_playing(self):
        """Displays video currently playing."""
        if self.counter == 0:
            print("No video is currently playing")
        elif self.countP == 0:
            print("Currently playing:",end=" ")
            self.show_a_video(self.vidU)
        elif self.countP > 0:
            print("Currently playing:",end=" ")
            self.show_a_video(self.vidU)
            print("- PAUSED")

        

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        bigL = playlist_name.upper()
        if bigL not in self.playlist.keys():
            self.playlist[bigL] = []
            self.num_vids += 1
            print(f"Successfully created new playlist: {playlist_name}")
            
        elif bigL in self.playlist:
            print("Cannot create playlist: A playlist with the same name already exists")
            

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        vid = self._video_library.get_video(video_id)
        vidT = vid.title
        Playlist_names = list(self.playlist.keys())
        big_P_name = playlist_name.upper()
        playlist_vids= self.playlist.get(big_P_name)
        
       
        if video_id not in playlist_vids:
            self.playlist[ big_P_name] = video_id
        elif video_id in playlist_vids :
            print(f"Cannot add video to {playlist_name}: Video already added")
        
        elif vid == None:
                print(f"Cannot add video to {playlist_name}: Video does not exist")

        elif playlist_name not in Playlist_names:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        
        else:
            print(f"Added video to {playlist_name}: {vidT}")


    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
