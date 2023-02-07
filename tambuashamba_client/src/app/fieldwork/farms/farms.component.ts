import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params, Router } from '@angular/router';
import { Farm } from '../models/farm.model';
import { SourceFile } from '../models/sourceFile.model';
import { FieldWorkService } from '../services/fieldwork.service';

@Component({
  selector: 'app-farms',
  templateUrl: './farms.component.html',
  styleUrls: ['./farms.component.css']
})
export class FarmsComponent implements OnInit {
  farmDetails: { count: number, next: string, previous: string, results: Farm[] } = { count: 4, next: "", previous: "", results: [] }
  fileDetails: SourceFile = { id: 0, title: "", file_slug: "", csv_file: "", farm_count: 0, created_at: "", updated_at: "" };


  constructor(private router: Router, private route: ActivatedRoute, private feildWorkService: FieldWorkService) { }
  ngOnInit() {

    this.route.params.subscribe((params: Params) => {
      this.feildWorkService.getFarmsOfSourceFile(params['fileId']).subscribe((response: any) => {

        this.farmDetails = response
      })

      this.feildWorkService.getSourceFileById(+params['fileId']).subscribe((response: any) => {
        this.fileDetails = response
      })

    })
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
