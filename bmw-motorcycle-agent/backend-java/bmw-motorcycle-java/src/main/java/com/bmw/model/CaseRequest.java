package com.bmw.model;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.Size;

public class CaseRequest {
    @NotBlank
    @Size(min = 2)
    private String dealerName;

    @NotBlank
    @Size(min = 2)
    private String customerName;

    @NotBlank
    @Size(min = 2)
    private String vehicleModel;

    @NotBlank
    @Size(min = 5)
    private String vin;

    @NotBlank
    @Size(min = 10)
    private String issueSummary;

    private String requestType = "service_request";

    public String getDealerName() {
        return dealerName;
    }

    public void setDealerName(String dealerName) {
        this.dealerName = dealerName;
    }

    public String getCustomerName() {
        return customerName;
    }

    public void setCustomerName(String customerName) {
        this.customerName = customerName;
    }

    public String getVehicleModel() {
        return vehicleModel;
    }

    public void setVehicleModel(String vehicleModel) {
        this.vehicleModel = vehicleModel;
    }

    public String getVin() {
        return vin;
    }

    public void setVin(String vin) {
        this.vin = vin;
    }

    public String getIssueSummary() {
        return issueSummary;
    }

    public void setIssueSummary(String issueSummary) {
        this.issueSummary = issueSummary;
    }

    public String getRequestType() {
        return requestType;
    }

    public void setRequestType(String requestType) {
        this.requestType = requestType;
    }
}
