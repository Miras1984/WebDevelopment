import { Component, OnInit } from '@angular/core';
import { Observable, of } from 'rxjs';
import { AlbumsService } from '../albums.service';
import { Album  } from '../Album_model';

@Component({
  selector: 'app-albums',
  templateUrl: './albums.component.html',
  styleUrls: ['./albums.component.css']
})
export class AlbumsComponent implements OnInit{
  albums: Album[] = [];

  constructor(private albumsService: AlbumsService){}

  Delete(id: number){
    this.albums = this.albums.filter((album) => album.id != id);
    this.albumsService.AlbumDelete(id).subscribe( () => {});
  }

  ngOnInit(){
    this.getAlbums();
  }

  
  getAlbums(){
    this.albumsService.getAlbums().subscribe( (albums) => {
      this.albums = albums;
    });
  }

}
