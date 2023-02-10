import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {
  constructor(private http: HttpClient) {}

  postData(url: string, data: any) {
    return this.http.post(url, data);
  }

  getData(url: string) {
    return this.http.get(url);
  }
}
