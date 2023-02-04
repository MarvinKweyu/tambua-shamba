import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  constructor(private httpClient: HttpClient) { }

  getAllFarms(): any {
    return this.httpClient.get(environment.baseUrl + "soilcarbon/farms/")
  }

  getBestFarms(count: number): any {
    http://127.0.0.1:8000/api/v1/soilcarbon/farms/topfarms/{count}/
    return this.httpClient.get(environment.baseUrl + `soilcarbon/farms/topfarms/${count}/`)
  }

  getWorstFarms(count: number): any {
    return this.httpClient.get(environment.baseUrl + `soilcarbon/farms/worstfarms/${count}/`)
  }
}
