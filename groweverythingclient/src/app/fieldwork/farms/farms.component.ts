import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Farm } from '../models/farm.model';
import { FieldWorkService } from '../services/fieldwork.service';

@Component({
  selector: 'app-farms',
  templateUrl: './farms.component.html',
  styleUrls: ['./farms.component.css']
})
export class FarmsComponent implements OnInit {

  farms: Farm[] = [{ id: 1, farm_name: "Lusaka farm", soil_organic_carbon: 3567, source_file: 2, created_at: "Wed, 01 Jan 2020 00:00:00 GMT", updated_at: "Wed, 01 Jan 2020 00:00:00 GMT" }]

  constructor(private router: Router, private route: ActivatedRoute, private feildWorkService: FieldWorkService) { }
  ngOnInit() {
    console.log(this.route.snapshot.params['fileId'])
    // this.route.params.subscribe((params: Params) => {
    //   this.farms = this.feildWorkService.getFarmsOfSourceFile(params['fileId'])
    // })
  }

  searchFarms(searchTerm: string) {
    searchTerm = searchTerm.trim()
    if (searchTerm.length != 0) {
      // this.feildWorkService.searchFarmsByName(searchTerm).subscribe((res: { results: any[]; }) => { 
      //   if (res.count) > 1 { }
      // })
      
    }
    
  }
}
