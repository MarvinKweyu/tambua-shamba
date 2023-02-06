import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FieldworkRoutingModule } from './fieldwork-routing.module';
import { FieldworkComponent } from './fieldwork.component';
import { MatDialogModule } from '@angular/material/dialog';


@NgModule({
  declarations: [
    FieldworkComponent
  ],
  imports: [
    CommonModule,
    FieldworkRoutingModule,
    MatDialogModule,
  ]
})
export class FieldworkModule { }
