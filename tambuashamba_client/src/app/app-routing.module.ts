import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: "", loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
  { path: 'history', loadChildren: () => import('./fieldwork/fieldwork.module').then(m => m.FieldworkModule) },
  { path: '**', redirectTo: "" } // catch everything else and go back home
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
