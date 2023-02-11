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
  worstFarms: Farm[] = [];

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

    this.dashboardService.getWorstFarms(3).pipe(map((res: { results: [] }) => {
      // only add farms that are not already in the best farms list. This is in case the farm array has less than 6 farms
      return res.results.filter((item: any) => { return this.farms.indexOf(item) == -1 });


    })).subscribe((res: any) => {

      this.worstFarms = res.results ? res.results : [];

      this.farms = [...this.farms, ...this.worstFarms]
    },

      (error: any) => {
        this.toastr.error(error.error.error, "Unable to fetch least performing farms at this time")
        return;
      })

  }

}
