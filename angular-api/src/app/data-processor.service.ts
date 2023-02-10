import { Injectable } from '@angular/core';
import { HttpService } from './http.service';
import { map } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataProcessorService {
  private API_URL = 'https://jsonplaceholder.typicode.com/posts';

  constructor(private httpService: HttpService) { }

  getData() {
    return this.httpService.getData(this.API_URL).pipe(
      map(posts => posts)
    );
  }

createPost(postData: any) {
  return this.httpService.postData(this.API_URL, postData).pipe(
    map((response: any) => {
      console.log(response);
      return response;
    })
  );
}

}
