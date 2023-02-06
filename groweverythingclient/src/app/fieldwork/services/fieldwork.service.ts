import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class FieldWorkService {


  constructor(private httpClient: HttpClient) { }

  getSourceFiles(): any {
    return this.httpClient.get(environment.baseUrl + "soilcarbon/sources/")
  }
}
