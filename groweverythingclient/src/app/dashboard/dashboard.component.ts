import { Component } from '@angular/core';
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

  constructor(public dialog: MatDialog, public dashboardService: DashboardService, private toastr: ToastrService) {
    this.collectFarms();
  }

  ngOnInit() {

  }

  /*
get the top 3 and worst three farms
*/
  collectFarms() {

    this.dashboardService.getBestFarms(3).subscribe((res: any) => {

      this.bestFarms = res.results;
      this.farms = [...this.farms, ...res.results]
    },
      (error: any) => {
        this.toastr.error(error.error.error, "Unable to fetch best farms at this time")
        return;
      })

    this.dashboardService.getWorstFarms(3).subscribe((res: any) => {
      this.worstFarms = res.results;
      this.farms = [...this.farms, ...res.results]
    },

      (error: any) => {
        this.toastr.error(error.error.error, "Unable to fetch least performing farms at this time")
        return;
      })

    //  in case the dataset is small, we stand the chance of returning the same data for least
    // and worst farms. remove duplicates in this event

    this.farms = [...new Set(this.farms)]

  }

}
