import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FarmsComponent } from './farms/farms.component';
import { FieldworkComponent } from './fieldwork.component';

const routes: Routes = [
  { path: '', component: FieldworkComponent },
  { path: ':fileId', component: FarmsComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FieldworkRoutingModule { }
