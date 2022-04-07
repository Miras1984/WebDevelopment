import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AlbumsService } from '../albums.service';
import { Photo } from '../Album_model';

@Component({
  selector: 'app-album-photos',
  templateUrl: './album-photos.component.html',
  styleUrls: ['./album-photos.component.css']
})
export class AlbumPhotosComponent implements OnInit {
  photos: Photo[] = [];

  constructor(private route: ActivatedRoute,
              private albumsService: AlbumsService,
              private location: Location) { }

  ngOnInit(): void {
    this.getPhotos();
  }

  getPhotos(){
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.albumsService.getPhotos(id).subscribe( (photos) => {
      this.photos = photos;
    })
  }

  ReturnBack(){
    this.location.back();
  }

}
