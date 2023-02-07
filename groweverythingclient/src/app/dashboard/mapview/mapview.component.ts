import { AfterViewInit, Component, OnInit, Input } from '@angular/core';
import * as L from 'leaflet';
import * as geojson from 'geojson';
import { Farm } from '../models/farm.model';

@Component({
  selector: 'app-mapview',
  templateUrl: './mapview.component.html',
  styleUrls: ['./mapview.component.css']
})
export class MapviewComponent implements OnInit, AfterViewInit {
  @Input() farms: Farm[] = [];

  private map!: L.Map | L.LayerGroup<any>;

  constructor() { }

  ngOnInit(): void {
  }
  ngAfterViewInit(): void {
    this.initMap();
  }

  private initMap(): void {
    this.map = L.map('map', {
      center: [0.9626017982631033, 38.13330124848599],
      zoom: 7
    });

    const tiles = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 18,
      minZoom: 3,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });

    tiles.addTo(this.map);
    this.addGeoJsonFeatures();
  }

  addGeoJsonFeatures() {

    this.farms.forEach(farmItem => {
      const popDetail = L.popup().setContent(`<p> Farm name: ${farmItem.farm_name} <br/> SOC(tonnes/hectare): ${farmItem.soil_organic_carbon}</p>`)
      const fillcolor = farmItem.isBestFarm ? 'green' : 'red';

      let geoJsonFeatures: geojson.FeatureCollection = farmItem.geographical_boundaries;
      // fill color based on performance
      L.geoJSON(geoJsonFeatures).bindPopup(popDetail).setStyle({ fillColor: fillcolor })
        .addTo(this.map);

    });
  }

}
