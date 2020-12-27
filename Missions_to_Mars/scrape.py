from flask import Flask

# NASA Mars News
news_title = "A Martian Roundtrip: NASA's Perseverance Rover Sample Tubes"
news_p = "Marvels of engineering, the rover's sample tubes must be tough enough to safely bring Red Planet samples on the long journey back to Earth in immaculate condition."

# JPL Mars Space Images - Featured Image
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA17462_ip.jpg'


# Mars Facts
table_html = '<table border="1" class="dataframe">\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>Mass:</td>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>Surface Temperature:</td>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>Diameter:</td>\n      <td>6,779 km</td>\n    </tr>\n    <tr>\n      <th>10</th>\n      <td>Mass:</td>\n      <td>6.39 × 10^23 kg</td>\n    </tr>\n    <tr>\n      <th>11</th>\n      <td>Moons:</td>\n      <td>2</td>\n    </tr>\n    <tr>\n      <th>12</th>\n      <td>Distance from Sun:</td>\n      <td>227,943,824 km</td>\n    </tr>\n    <tr>\n      <th>13</th>\n      <td>Length of Year:</td>\n      <td>687 Earth days</td>\n    </tr>\n    <tr>\n      <th>14</th>\n      <td>Temperature:</td>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <th>15</th>\n      <td>Equatorial Diameter:</td>\n      <td>6,792 km</td>\n    </tr>\n    <tr>\n      <th>16</th>\n      <td>Polar Diameter:</td>\n      <td>6,752 km</td>\n    </tr>\n    <tr>\n      <th>17</th>\n      <td>Mass:</td>\n      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n    </tr>\n    <tr>\n      <th>18</th>\n      <td>Moons:</td>\n      <td>2 (Phobos &amp; Deimos)</td>\n    </tr>\n    <tr>\n      <th>19</th>\n      <td>Orbit Distance:</td>\n      <td>227,943,824 km (1.38 AU)</td>\n    </tr>\n    <tr>\n      <th>20</th>\n      <td>Orbit Period:</td>\n      <td>687 days (1.9 years)</td>\n    </tr>\n    <tr>\n      <th>21</th>\n      <td>Surface Temperature:</td>\n      <td>-87 to -5 °C</td>\n    </tr>\n    <tr>\n      <th>22</th>\n      <td>First Record:</td>\n      <td>2nd millennium BC</td>\n    </tr>\n    <tr>\n      <th>23</th>\n      <td>Recorded By:</td>\n      <td>Egyptian astronomers</td>\n    </tr>\n  </tbody>\n</table>'

# Mars Hemispheres
hemisphere_image_urls = [{'title': 'Cerberus Hemisphere',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'},
 {'title': 'Schiaparelli Hemisphere',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'},
 {'title': 'Syrtis Major Hemisphere',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'},
 {'title': 'Valles Marineris Hemisphere',
  'img_url': 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]


