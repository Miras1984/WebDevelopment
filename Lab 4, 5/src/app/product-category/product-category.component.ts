import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { Product, products } from '../products';

@Component({
  selector: 'app-product-category',
  templateUrl: './product-category.component.html',
  styleUrls: ['./product-category.component.css']
})
export class ProductCategoryComponent implements OnInit {
  item : Product | undefined;
  items: Product[] = [];
  Like: number = 0;

  share() {
    window.alert('The product has been shared!');
  }

  onNotify(){
    window.alert('You will be notified when the product goes on sale');
  }

  delete(key : Product){
    const index = this.items.indexOf(key, 0);
    if (index > -1){
      this.items.splice(index, 1);
    }
  }

  AddLike(prod : Product){
    prod.NumberLikes++;
  }

  constructor(private route: ActivatedRoute) { }

  ngOnInit(){
    const routeParams = this.route.snapshot.paramMap;
    const productCatFromRoute = String(routeParams.get('productCat'));

    for(let a of products){
      if(a.category === productCatFromRoute){
        this.items.push(a);
      }
    }
  }
}
