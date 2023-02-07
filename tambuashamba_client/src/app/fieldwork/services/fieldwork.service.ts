import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
@Injectable({
  providedIn: 'root'
})
export class FieldWorkService {
  constructor(private httpClient: HttpClient) { }

  /*
  Get all the files uploaded by the user that contain farm data
  */
  getSourceFiles(): any {
    return this.httpClient.get(environment.baseUrl + "soilcarbon/sources/")
  }


  getSourceFileById(fileId: number): any {
    return this.httpClient.get(environment.baseUrl + "soilcarbon/sources/" + fileId)
  }

  /*
  Get all the farms related to a file
  */
  getFarmsOfSourceFile(fileId: string): any {
    // ?source_file__id = 1
    return this.httpClient.get(environment.baseUrl + "soilcarbon/farms/?source_file__id=" + fileId)
  }
  /*
  Search for a farm by farm name
  */
  searchFarmsByName(searchTerm: string) {
    return this.httpClient.get(environment.baseUrl + "soilcarbon/farms/search?search=" + searchTerm)
  }

  /*
Search for a farm by farm soil carbon content
*/
  searchFarmsBySoilCarbon(searchTerm: string) {
    return this.httpClient.get(environment.baseUrl + "soilcarbon/farms/search?search=" + searchTerm)
  }


}
