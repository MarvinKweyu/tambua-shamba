import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FieldworkComponent } from './fieldwork.component';

const routes: Routes = [{ path: '', component: FieldworkComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FieldworkRoutingModule { }
