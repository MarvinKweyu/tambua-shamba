import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { FieldworkRoutingModule } from './fieldwork-routing.module';
import { FieldworkComponent } from './fieldwork.component';
import { MatDialogModule } from '@angular/material/dialog';
import { FarmsComponent } from './farms/farms.component';


@NgModule({
  declarations: [
    FieldworkComponent,
    FarmsComponent
  ],
  imports: [
    CommonModule,
    FieldworkRoutingModule,
    MatDialogModule,
  ]
})
export class FieldworkModule { }
