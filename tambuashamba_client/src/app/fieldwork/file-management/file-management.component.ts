import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpEventType, HttpResponse } from "@angular/common/http";
import { ToastrService } from 'ngx-toastr';
import { environment } from 'src/environments/environment';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-file-management',
  templateUrl: './file-management.component.html',
  styleUrls: ['./file-management.component.css']
})
export class FileManagementComponent implements OnInit {
  uploadUrl: string = environment.baseUrl + "soilcarbon/sources/"

  percentDone: any = "";
  failedUpload: boolean = false;

  constructor(
    private httpClient: HttpClient,
    public dialogRef: MatDialogRef<FileManagementComponent>,
    private toastr: ToastrService
  ) {
  }

  ngOnInit(): void {
  }

  uploadFile(event: Event) {
    // @ts-ignore
    if (!event.target.files) {
      return
    }

    const formData = new FormData();

    // @ts-ignore
    formData.append("csv_file", event.target["files"][0]);

    this.httpClient
      .post(this.uploadUrl, formData)
      .subscribe((response: any) => {
        this.closeDialog();
        this.toastr.success("File uploaded successfully", "Uploaded!")

      },
        error => {
          this.failedUpload = true;
          this.toastr.error(error.error.error, "Unable to upload file")
          return;
        });
  }

  closeDialog() {
    this.dialogRef.close();
  }

}
