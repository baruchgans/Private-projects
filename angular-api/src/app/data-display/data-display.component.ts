import {Component, OnInit} from '@angular/core';
import {DataProcessorService} from '../data-processor.service';


@Component({
  selector: 'app-data-display',
  templateUrl: './data-display.component.html',
  styleUrls: ['./data-display.component.scss']
})
export class DataDisplayComponent implements OnInit {
  posts: any;
  postData = {title: '', body: ''};

  constructor(private dataProcessorService: DataProcessorService) {
  }

  ngOnInit() {
    this.dataProcessorService.getData().subscribe(posts => {
      this.posts = posts;
    });
  }

  createPost() {
    this.dataProcessorService.createPost(this.postData).subscribe((response: any) => {
      console.log(response);
      this.posts.push(response);
      this.postData = {title: '', body: ''}
    });
  }

}
