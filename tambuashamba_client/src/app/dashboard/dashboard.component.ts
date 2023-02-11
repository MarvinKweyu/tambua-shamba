import { Component } from '@angular/core';
import { map } from 'rxjs/operators'
import { MatDialog } from '@angular/material/dialog';
import { ToastrService } from 'ngx-toastr';
import { Farm } from './models/farm.model';
import { DashboardService } from './services/dashboard.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {

  farms: Farm[] = [];
  bestFarms: Farm[] = [];
  worstFarms: Farm[] | undefined;

  constructor(
    public dialog: MatDialog,
    public dashboardService: DashboardService,
    private toastr: ToastrService) {
  }

  ngOnInit() {
    this.collectFarms();
  }

  /*
get the top 3 and worst three farms
*/
  collectFarms() {

    this.dashboardService.getBestFarms(3).pipe(map((res: { results: [] }) => {
      // add a tag on each to show that it is one of the best farms
      res.results.forEach((farm: Farm) => { farm.isBestFarm = true })
      return res;
    })).subscribe((res: any) => {

      this.bestFarms = res.results;
      this.farms = [...this.farms, ...this.bestFarms]

    },
      (error: any) => {
        this.toastr.error(error.error.error, "Unable to fetch best farms at this time")
        return;
      })

    this.dashboardService.getWorstFarms(3).pipe(map((res: { results: any }) => {

      // only add farms that are not already in the best farms list. This is in case the farm array has less than 6 farms
      const results = res.results.filter((item: any) => {
        return this.bestFarms.indexOf(item) == -1;
      });
      res.results = results ? results : [];

      return res;


    })).subscribe((res: any) => {

      this.worstFarms = res.results;
      // before a spread, check if the array is undefined else have it as empty array
      // * note the definition on the worst farms variable
      let worst: Farm[] = this.worstFarms || [];
      this.farms = [...this.farms, ...worst]


    },

      (error: any) => {
        this.toastr.error(error.error.error, "Unable to fetch least performing farms at this time")
        return;
      })

  }

}
