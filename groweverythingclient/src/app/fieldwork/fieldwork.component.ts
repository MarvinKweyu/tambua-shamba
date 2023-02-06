import { Component } from '@angular/core';
import { ToastrService } from 'ngx-toastr';
import { MatDialog } from '@angular/material/dialog';
import { FileManagementComponent } from 'src/app/fieldwork/file-management/file-management.component';
import { FieldWorkService } from './services/fieldwork.service';
import { SourceFile } from './models/sourceFile.model';


@Component({
  selector: 'app-fieldwork',
  templateUrl: './fieldwork.component.html',
  styleUrls: ['./fieldwork.component.css']
})
export class FieldworkComponent {
  allFiles: SourceFile[] = [];

  constructor(public dialog: MatDialog, public fieldWorkService: FieldWorkService, private toastr: ToastrService) { }

  ngOnInit(): void {
    this.getFiles()
  }

  getFiles(): void {
    this.fieldWorkService.getSourceFiles().subscribe((res: { results: any[]; }) => {
      this.allFiles = res.results
    },
      // @ts-ignore
      error => {
        this.toastr.error(error.error.error, "Unable to retrieve uploaded files")
      }
    )
  }


  uploadFile() {
    const dialogRef = this.dialog.open(FileManagementComponent, {
      height: '300px',
      width: '300px',
      panelClass: 'icon-outside',
    });

    dialogRef.afterClosed().subscribe(result => {
      this.getFiles()
    });
  }

}
