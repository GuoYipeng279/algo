#include <stdio.h>
#include <iostream>
using namespace std;

class vec3{
public:
    float x;
    float y;
    float z;
    vec3(float x, float y,float z){
        x = x;
        y = y;
        z = z;
    }
};

class vec4{
public:
    vec3 xyz;
    float w;
    vec4(float x, float y,float z,float w){
        xyz = vec3(x,y,z);
        w = w;
    }
};

vec3 RGB_HSV(vec3 rgb){
    vec3 hsv = vec3(0.0,0.0,0.0);
    hsv.z = max(rgb.x,max(rgb.y,rgb.z));
    float rgb_min = min(rgb.x,min(rgb.y,rgb.z));
    hsv.y = (hsv.z-rgb_min)/hsv.z;
    if (rgb_min==rgb.z){
        hsv.x = 120.0*(rgb.y-rgb_min)/(rgb.x+rgb.y-2.0*rgb_min);
    }else if (rgb_min==rgb.x){
        hsv.x = 120.0*(rgb.z-rgb_min)/(rgb.z+rgb.y-2.0*rgb_min)+120.0;
    }else {
        hsv.x = 120.0*(rgb.x-rgb_min)/(rgb.z+rgb.x-2.0*rgb_min)+240.0;
    }
    return hsv;
};

vec3 HSV_RGB(vec3 hsv){
    vec3 rgb = vec3(0.0,0.0,0.0);
    float max_rgb = hsv.z;
    float min_rgb = (1.0-hsv.y)*max_rgb;
    float H = hsv.x;
    if (hsv.x<120.0){
        rgb.z = min_rgb;
        float gb_rb = 120.0/H-1.0;
        if (gb_rb>1.0){
        rgb.y = max_rgb;
        rgb.x = (max_rgb-min_rgb)/gb_rb+min_rgb;
        }else{
        rgb.x = max_rgb;
        rgb.y = (max_rgb-min_rgb)*gb_rb+min_rgb;
        }
    }else if (hsv.x<240.0){
        rgb.x = min_rgb;
        H -= 120.0;
        float br_gr = 120.0/H-1.0;
        if (br_gr>1.0){
        rgb.z = max_rgb;
        rgb.y = (max_rgb-min_rgb)/br_gr+min_rgb;
        }else{
        rgb.y = max_rgb;
        rgb.z = (max_rgb-min_rgb)*br_gr+min_rgb;
        }
    }else{
        rgb.y = min_rgb;
        H -= 240.0;
        float rg_bg = 120.0/H-1.0;
        if (rg_bg>1.0){
        rgb.x = max_rgb;
        rgb.z = (max_rgb-min_rgb)/rg_bg+min_rgb;
        }else{
        rgb.z = max_rgb;
        rgb.x = (max_rgb-min_rgb)*rg_bg+min_rgb;
        }
    }
    return rgb;
};

//main program for each fragment = pixel candidate
void main() {
  vec3 rgb = vec3(0.0,0.0,1.0);
  rgb = HSV_RGB(RGB_HSV(rgb));
  std::cout << vec4(rgb, 1.0);
  return 0;
}